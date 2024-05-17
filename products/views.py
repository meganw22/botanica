from django.shortcuts import render, get_object_or_404
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