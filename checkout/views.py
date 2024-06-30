from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm, AddressForm
from .models import Order, OrderItem
from user_profile.models import Address
from products.models import Product, PlantPrice
from bag.contexts import bag_contents
import stripe
import json
from django.db import IntegrityError
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from .webhook_handler import StripeWH_Handler


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag')),
            'username': request.user.username,
        })
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        messages.error(request, 'Sorry, your payment cannot be processed \
            at this time. Please try again later.')
        return HttpResponse(content=str(e), status=400)


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

    user = request.user
    addresses = Address.objects.filter(user=user)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        address_form = AddressForm(request.POST)

        selected_address_id = request.POST.get('selected_address')
        if selected_address_id:
            address = Address.objects.get(id=selected_address_id, user=user)
        else:
            address = None

        if order_form.is_valid() and (selected_address_id or address_form.is_valid()):
            order = order_form.save(commit=False)
            order.user = user
            order.email_address = user.email
            if selected_address_id:
                order.address = address
            else:
                address = address_form.save(commit=False)
                address.user = user
                address.save()
                order.address = address

            client_secret = request.POST.get('client_secret')
            if client_secret:
                order.stripe_pid = client_secret.split('_secret')[0]

            try:
                order.save()

                # Save the order items
                for item in bag:
                    product = Product.objects.get(id=item['id'])
                    price = PlantPrice.objects.get(
                        product=product, size=item['height']).price
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_size=item['height'],
                        quantity_ordered=item['quantity'],
                        item_total=Decimal(price) * item['quantity'],
                    )

                # Clear the bag items from the session
                request.session['bag'] = []

                messages.success(
                    request, f"Order {order.order_id} placed successfully!")
                return redirect('checkout_success', order_id=order.order_id)
            except IntegrityError:
                messages.error(
                    request, "An error occurred while placing the order.")
                return redirect('checkout')
        else:
            messages.error(
                request,
                "There was an error with your form."
                "Please check your information.")
    else:
        order_form = OrderForm()
        address_form = AddressForm()

    if not stripe_public_key:
        messages.warning(
            request,
            'Stripe public key is missing.'
            'Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'address_form': address_form,
        'addresses': addresses,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    context.update(bag_contents(request))
    return render(request, template, context)


@login_required
def checkout_success(request, order_id):
    """View for a successful checkout"""
    try:
        order = Order.objects.get(order_id=order_id)

        context = {
            'order': order,
        }
        return render(request, 'checkout/checkout_success.html', context)
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('checkout')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Set up a Stripe webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the event type from Stripe
    event_type = event['type']

    # Get the handler function for the event type
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
