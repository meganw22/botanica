from decimal import Decimal
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm, AddressForm
from .models import Order, OrderItem
from user_profile.models import Address, UserProfile
from products.models import Product, PlantPrice
from bag.contexts import bag_contents
import stripe
from django.db import IntegrityError

@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', [])
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect('products')

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = int(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        address_form = AddressForm(request.POST)
        if order_form.is_valid() and address_form.is_valid():
            order = order_form.save(commit=False)
            address = address_form.save()
            address.user = request.user
            address.save()
            order.address = address
            order.user = request.user
            order.email_address = request.user.email
            client_secret = request.POST.get('client_secret')
            if client_secret:
                order.stripe_pid = client_secret.split('_secret')[0]
            try:
                order.save()

                # Save the order items
                for item in bag:
                    product = Product.objects.get(id=item['id'])
                    price = PlantPrice.objects.get(product=product, size=item['height']).price
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_size=item['height'],
                        quantity_ordered=item['quantity'],
                        item_total=Decimal(price) * item['quantity'],
                    )

                # Update user's default address
                user_profile, created = UserProfile.objects.get_or_create(user=request.user)
                user_profile.default_address = address
                user_profile.save()

                # Clear the bag items from the session
                request.session['bag'] = []

                messages.success(request, f"Order {order.order_id} placed successfully!")
                return redirect('checkout_success', client_secret=client_secret)
            except IntegrityError:
                messages.error(request, "An error occurred while placing the order.")
                return redirect('checkout')
        else:
            messages.error(request, "There was an error with your form. Please check your information.")
    else:
        order_form = OrderForm()
        address_form = AddressForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'address_form': address_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    context.update(bag_contents(request))

    return render(request, template, context)

@login_required
def checkout_success(request, client_secret):
    stripe_pid = client_secret.split('_secret')[0]

    try:
        order = Order.objects.get(stripe_pid=stripe_pid)

        context = {
            'order': order,
        }
        return render(request, 'checkout/checkout_success.html', context)
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('checkout')