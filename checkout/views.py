from decimal import Decimal
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product, PlantPrice
from user_profile.models import UserProfile
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
        return redirect(reverse('products'))

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
        if order_form.is_valid():
            order = order_form.save(commit=False)
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

                messages.success(request, f"Order {order.order_id} placed successfully!")
                return redirect(reverse('checkout_success', kwargs={'client_secret': client_secret}))
            except IntegrityError:
                messages.error(request, "An order with this Stripe payment already exists.")
                return redirect(reverse('checkout'))
        else:
            messages.error(request, "There was an error with your form. Please check your information.")
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
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

        profile, created = UserProfile.objects.get_or_create(user=request.user)

        profile.default_phone_number = order.contact_number
        profile.default_street_address1 = order.street_address1
        profile.default_street_address2 = order.street_address2
        profile.default_town_or_city = order.town_city
        profile.default_county = order.county
        profile.default_postcode = order.postcode
        profile.default_country = order.country
        profile.save()

        context = {
            'order': order,
        }
        return render(request, 'checkout/checkout_success.html', context)
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect(reverse('checkout'))
