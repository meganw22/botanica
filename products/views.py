from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, PlantSize, PlantPrice


def all_products(request):
    """
    View to display all products.
    """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to display the details of a specific product.
    """
    product = get_object_or_404(Product, pk=product_id)

    heights = {}
    for size in ['sm', 'md', 'lg']:
        plant_size = PlantSize.objects.filter(plant=product, size=size).first()
        heights[size] = plant_size.height if plant_size else 'N/A'

    plant_prices = PlantPrice.objects.filter(product=product)
    prices = {price.size: price.price for price in plant_prices}

    smallest_price = min(prices.values()) if prices else None

    context = {
        'product': product,
        'heights': heights,
        'prices': prices,
        'smallest_price': smallest_price,
    }
    return render(request, 'products/product_detail.html', context)


def filter_products(request):
    """
    View to filter products by light, pet safety, ease of care, and price.
    """
    light = request.GET.get('light', '')
    pet_ok = request.GET.get('pet_ok', '')
    ease_of_care = request.GET.get('ease_of_care', '')
    price = request.GET.get('price', '')

    if not light and not pet_ok and not ease_of_care and not price:
        return redirect('products')

    products = Product.objects.all()

    if light:
        products = products.filter(light=light)
    if pet_ok:
        products = products.filter(pet_ok=(pet_ok == 'true'))
    if ease_of_care:
        products = products.filter(ease_of_care=ease_of_care)
    if price:
        plant_prices = PlantPrice.objects.filter(price__lte=price)
        product_ids = plant_prices.values_list('product_id', flat=True)
        products = products.filter(id__in=product_ids)

    context = {
        'products': products,
    }
    return render(request, 'products/filter_products.html', context)


def filter_category_products(request, light=None,  ease_of_care=None,
                             size=None, order=None):
    """
    View to filter products by light, ease of care, size, and order.
    """
    products = Product.objects.all()
    category = "Filtered"

    if light:
        products = products.filter(light=light)
        if light == 'bright':
            category = "Bright Light"
        elif light == 'low':
            category = "Low Light"
    if ease_of_care:
        products = products.filter(ease_of_care=ease_of_care)
        if ease_of_care == 'easy':
            category = "Easy Maintenance"
        elif ease_of_care == 'difficult':
            category = "For the Expert Plant Carers"
    if size:
        plant_sizes = PlantSize.objects.filter(size=size)
        product_ids = plant_sizes.values_list('plant_id', flat=True)
        products = products.filter(id__in=product_ids)
        if size == 'sm':
            category = "Baby Plants"
        elif size == 'lg':
            category = "Big Plants"
    if order == 'price_asc':
        products = products.order_by('prices__price')
        category = "Lowest to Highest Price"
    elif order == 'price_desc':
        products = products.order_by('-prices__price')
        category = "Highest to Lowest Prices"

    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'products/filter_categories.html', context)
