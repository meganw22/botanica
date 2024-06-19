from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import OrderForm
from .models import Order
from bag.contexts import bag_contents
import stripe

@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
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
            order.stripe_pid = intent.id
            order.original_bag = bag

            # Save the order and redirect to the success page
            order.save()
            messages.success(request, "Order placed successfully!")
            return redirect(reverse('checkout_success'))
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
def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')
