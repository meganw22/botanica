from django.http import HttpResponse
from .models import Order, OrderItem
from products.models import Product, PlantPrice
from decimal import Decimal
import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event['data']['object']
        pid = intent['id']
        metadata = intent['metadata']
        bag = json.loads(metadata['bag'])
        username = metadata['username']
        save_info = metadata.get('save_info', False)

        billing_details = intent['charges']['data'][0]['billing_details']
        shipping_details = intent['shipping']
        grand_total = round(intent['amount_received'] / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details['address'].items():
            if value == "":
                shipping_details['address'][field] = None

        order_exists = False
        order = None
        attempts = 0

        while attempts < 5:
            try:
                order = Order.objects.get(
                    customer_name__iexact=shipping_details['name'],
                    email_address__iexact=billing_details['email'],
                    phone_number__iexact=shipping_details['phone'],
                    country__iexact=shipping_details['address']['country'],
                    postcode__iexact=shipping_details['address']['postal_code'],
                    town_or_city__iexact=shipping_details['address']['city'],
                    street_address1__iexact=shipping_details['address']['line1'],
                    street_address2__iexact=shipping_details['address']['line2'],
                    county__iexact=shipping_details['address']['state'],
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempts += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order in database',
                status=200)

        if not order_exists:
            try:
                order = Order.objects.create(
                    customer_name=shipping_details['name'],
                    email_address=billing_details['email'],
                    phone_number=shipping_details['phone'],
                    country=shipping_details['address']['country'],
                    postcode=shipping_details['address']['postal_code'],
                    town_or_city=shipping_details['address']['city'],
                    street_address1=shipping_details['address']['line1'],
                    street_address2=shipping_details['address']['line2'],
                    county=shipping_details['address']['state'],
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                
                for item_id, item_data in bag.items():
                    product = Product.objects.get(id=item_id)
                    price = PlantPrice.objects.get(product=product, size=item_data['size']).price
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        product_size=item_data['size'],
                        quantity_ordered=item_data['quantity'],
                        item_total=Decimal(price) * item_data['quantity'],
                    )

                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                    status=200)

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=str(e), status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200)