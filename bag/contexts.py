from django.conf import settings

def bag_contents(request):
    bag = request.session.get('bag', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in bag)
    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    delivery_cost = 0 if total_price >= free_delivery_threshold else settings.STANDARD_DELIVERY_COST
    grand_total = total_price + delivery_cost

    context = {
        'bag': bag,
        'total_price': total_price,
        'free_delivery_threshold': free_delivery_threshold,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
    }

    return context