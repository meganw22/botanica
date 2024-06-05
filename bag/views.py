from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product, PlantPrice

# Add to bag view
def add_to_bag(request, product_id):
    
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    selected_height = request.POST.get('selected_height')

    if not selected_height:
        messages.error(request, 'Please select a height before adding to the bag.')
        return redirect(request.META.get('HTTP_REFERER'))

    try:
        price = PlantPrice.objects.get(product=product, size=selected_height).price
    except PlantPrice.DoesNotExist:
        messages.error(request, 'Invalid height selected.')
        return redirect(request.META.get('HTTP_REFERER'))

    bag = request.session.get('bag', [])
    for item in bag:
        if item['id'] == product_id and item.get('height') == selected_height:
            item['quantity'] += quantity
            messages.success(request, f'Updated quantity for {product.easy_name} ({selected_height}).')
            break
    else:
        bag.append({
            'id': product.id,
            'name': product.easy_name,
            'quantity': quantity,
            'height': selected_height,
            'image_url': product.image.url if product.image else '/default_images/no-image-available.png',
            'price': float(price)
        })
        messages.success(request, f'Added {product.easy_name} ({selected_height}) to the bag.')

    request.session['bag'] = bag

    return redirect(request.META.get('HTTP_REFERER'))

# Shopping bag view
def shopping_bag(request):
    context = {
        'bag': request.session.get('bag', [])
    }
    return render(request, 'bag/bag.html', context)

# Remove from bag view
def remove_from_bag(request, product_id, height):
    bag = request.session.get('bag', [])
    updated_bag = [item for item in bag if not (item['id'] == product_id and item['height'] == height)]
    request.session['bag'] = updated_bag
    messages.success(request, 'Removed item from the bag.')
    return redirect(request.META.get('HTTP_REFERER'))
