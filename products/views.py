from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product

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

    context = {
        'product': product
    }
    
    return render(request, 'products/product_detail.html', context)

# Filter Products
def filter_products(request):
    light = request.GET.get('light', '')
    height = request.GET.get('height', '')
    ease_of_care = request.GET.get('ease_of_care', '')
    price = request.GET.get('price', '')

    # Check if all filters are empty or "All"
    if not light and not height and not ease_of_care and not price:
        return redirect('products')

    products = Product.objects.all()

    if light:
        products = products.filter(light=light)
    if height:
        products = products.filter(height=height)
    if ease_of_care:
        products = products.filter(ease_of_care=ease_of_care)
    if price:
        products = products.filter(price__lte=price)

    context = {
        'products': products,
    }
    return render(request, 'products/filter_products.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
