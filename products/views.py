from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, PlantSize, PlantPrice

# All Products Views
def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


# Product detail View
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Fetch heights
    heights = {}
    for size in ['sm', 'med', 'lg']:
        plant_size = PlantSize.objects.filter(plant=product, size=size).first()
        heights[size] = plant_size.height if plant_size else 'N/A'
    
    # Fetch prices
    plant_prices = PlantPrice.objects.filter(product=product)
    prices = {price.size: price.price for price in plant_prices}
    
    # Find the smallest price
    smallest_price = min(prices.values()) if prices else None

    context = {
        'product': product,
        'heights': heights,
        'prices': prices,
        'smallest_price': smallest_price,
    }
    return render(request, 'products/product_detail.html', context)

# Filter Products views
def filter_products(request):
    light = request.GET.get('light', '')
    height = request.GET.get('height', '')
    ease_of_care = request.GET.get('ease_of_care', '')
    price = request.GET.get('price', '')

    if not light and not height and not ease_of_care and not price:
        return redirect('products')

    products = Product.objects.all()

    if light:
        products = products.filter(light=light)
    if height:
        plant_sizes = PlantSize.objects.filter(height=height)
        product_ids = plant_sizes.values_list('plant_id', flat=True)
        products = products.filter(id__in=product_ids)
    if ease_of_care:
        products = products.filter(ease_of_care=ease_of_care)
    if price:
        products = products.filter(price__lte=price)

    context = {
        'products': products,
    }
    return render(request, 'products/filter_products.html', context)


    bag = request.session.get('bag', [])
    print(f"Initial bag: {bag}")
    updated_bag = [item for item in bag if not (item['id'] == product_id and item['height'] == height)]
    request.session['bag'] = updated_bag
    print(f"Updated bag: {updated_bag}")
    return redirect('shopping_bag')