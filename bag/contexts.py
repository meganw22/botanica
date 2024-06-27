from decimal import Decimal
from django.conf import settings
from products.models import Product, PlantPrice


def bag_contents(request):
    """
    Calculate and return the contents of the shopping bag including
    total price, total quantity, delivery cost, and grand total.
    """
    # Calculate the total price of items in the bag
    bag = request.session.get('bag', [])
    total_price = Decimal('0.00')
    for item in bag:
        product = Product.objects.get(id=item['id'])
        price = PlantPrice.objects.get(
            product=product, size=item['height']
            ).price
        total_price += Decimal(price) * item['quantity']

    total_quantity = sum(item['quantity'] for item in bag)
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)

    # Determine the delivery cost
    delivery_cost = (
        Decimal('0.00')
        if total_price >= free_delivery_threshold
        else Decimal(settings.STANDARD_DELIVERY_COST)
    )
    grand_total = total_price + delivery_cost

    context = {
        'bag': bag,
        'total_price': total_price,
        'total_quantity': total_quantity,
        'free_delivery_threshold': free_delivery_threshold,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context
