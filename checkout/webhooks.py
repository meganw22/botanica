import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
from .models import Order

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase
        handle_checkout_session(session)

    # Passed signature verification
    return HttpResponse(status=200)

def handle_checkout_session(session):
    # Retrieve the order using the session ID
    try:
        order = Order.objects.get(stripe_pid=session['payment_intent'])
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    # Check if the order has already been processed to avoid duplication
    if not order.processed:
        # Mark the order as processed
        order.processed = True
        order.save()

        # Add additional processing logic here (e.g., sending email confirmation)

        # Example: Avoid duplicate address creation
        if order.address and not order.address.user:
            address = order.address
            address.user = order.user
            address.save()
