from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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
    sizes = product.sizes.all()
    heights = {size.size: size.height for size in sizes}
    context = {
        'product': product,
        'heights': heights,
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
        products = products.filter(height=height)
    if ease_of_care:
        products = products.filter(ease_of_care=ease_of_care)
    if price:
        products = products.filter(price__lte=price)

    context = {
        'products': products,
    }
    return render(request, 'products/filter_products.html', context)


# Add to bag views
def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    selected_height = request.POST.get('selected_height')

    if not selected_height:
        messages.error(request, 'Please select a height before adding to the bag.')
        return redirect('product_detail', product_id=product_id)

    bag = request.session.get('bag', [])
    print(f"Initial bag: {bag}")

    # Check if the product is already in the bag
    for item in bag:
        if item['id'] == product_id and item.get('height') == selected_height:
            item['quantity'] += quantity
            break
    else:
        bag.append({
            'id': product.id,
            'name': product.easy_name,
            'price': float(product.price),
            'quantity': quantity,
            'height': selected_height,
            'image_url': product.image.url if product.image else '/default_images/no-image-available.png',
        })

    request.session['bag'] = bag
    print(f"Updated bag: {bag}")

    return redirect('shopping_bag')


#Shopping bag views
def shopping_bag(request):
    bag = request.session.get('bag', [])
    context = {
        'bag': bag,
    }
    return render(request, 'products/bag.html', context)

# Remove from bag
def remove_from_bag(request, product_id, height):
    bag = request.session.get('bag', [])
    print(f"Initial bag: {bag}")
    updated_bag = [item for item in bag if not (item['id'] == product_id and item['height'] == height)]
    request.session['bag'] = updated_bag
    print(f"Updated bag: {updated_bag}")
    return redirect('shopping_bag')