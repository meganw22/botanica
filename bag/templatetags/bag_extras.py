from django import template

register = template.Library()

@register.filter
def total_price(bag):
    return sum(item['price'] * item['quantity'] for item in bag)