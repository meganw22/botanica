from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product, PlantPrice
from django.urls import reverse
from django.utils.html import format_html


def add_to_bag(request, product_id):
    """
    Add a plant to the shopping bag with height and quantity
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    selected_height = request.POST.get('selected_height')

    if not selected_height:
        messages.error(
            request, 'Please select a height before adding to the bag.'
            )
        return redirect(request.META.get('HTTP_REFERER'))

    try:
        price = PlantPrice.objects.get(
            product=product, size=selected_height).price
    except PlantPrice.DoesNotExist:
        messages.error(request, 'Invalid height selected.')
        return redirect(request.META.get('HTTP_REFERER'))

    bag = request.session.get('bag', [])
    for item in bag:
        if item['id'] == product_id and item.get('height') == selected_height:
            item['quantity'] += quantity
            messages.success(
                request,
                format_html(
                    'Updated quantity: {}x {} ({}). '
                    '<div class="mt-auto d-flex justify-content-between '
                    'align-items-center"><a href="{}" class="btn '
                    'btn-custom-success">Go to Bag</a></div>',
                    item["quantity"], product.easy_name, selected_height,
                    reverse("shopping_bag")
                )
            )
            break
    else:
        new_item = {
            'id': product.id,
            'name': product.easy_name,
            'quantity': quantity,
            'height': selected_height,
            'image_url': (
                product.image.url
                if product.image
                else '/default_images/no-image-available.png'),
            'price': float(price)
        }
        bag.append(new_item)
        messages.success(
            request,
            format_html(
                'Added {}x {} ({}) to the bag. <div class="mt-auto d-flex '
                'justify-content-between align-items-center"><a href="{}" '
                'class="btn btn-custom-success">Go to Bag</a></div>',
                new_item["quantity"], product.easy_name, selected_height,
                reverse("shopping_bag")
            )
        )

    request.session['bag'] = bag

    return redirect(request.META.get('HTTP_REFERER'))


def adjust_bag(request, product_id):
    """
    Adjust the quantity of a specific item in the bag
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    selected_height = request.POST.get('selected_height', None)

    bag = request.session.get('bag', [])
    for item in bag:
        if item['id'] == product_id and item.get('height') == selected_height:
            if quantity > 0:
                item['quantity'] = quantity
                messages.success(
                    request,
                    f'Updated quantity: {item["quantity"]}x '
                    f'{product.easy_name} ({selected_height}).'
                    )
            else:
                bag.remove(item)
                messages.success(
                    request,
                    f'Removed {product.easy_name} '
                    f'({selected_height}) from the bag.'
                    )
            break
    else:
        messages.error(
            request,
            f'Could not find {product.easy_name} '
            f'({selected_height}) in your bag.'
            )

    request.session['bag'] = bag

    return redirect(reverse('shopping_bag'))


def shopping_bag(request):
    """
    Get the shopping bag view
    """
    context = {
        'bag': request.session.get('bag', [])
    }
    return render(request, 'bag/bag.html', context)


def remove_from_bag(request, product_id, height):
    """
    Remove an item in the shopping bag
    """
    bag = request.session.get('bag', [])
    updated_bag = [
        item for item in bag
        if not (item['id'] == product_id and item['height'] == height)
    ]
    request.session['bag'] = updated_bag
    messages.success(request, 'Removed item from the bag.')
    return redirect(request.META.get('HTTP_REFERER'))
