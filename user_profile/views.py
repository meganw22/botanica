from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from checkout.models import Order
from django_countries import countries
from django.contrib import messages
from itertools import groupby


def get_unique_addresses(addresses):
    """Ensure no duplicate addresses are shown"""
    unique_addresses = []
    seen_addresses = set()
    for address in addresses:
        full_address = (
            address.phone_number,
            address.street_address1,
            address.street_address2,
            address.town_or_city,
            address.county,
            address.postcode,
            address.country.name
        )
        if full_address not in seen_addresses:
            seen_addresses.add(full_address)
            unique_addresses.append(address)
    return unique_addresses


@login_required
def profile(request):
    """
    User Profile View: Display the user's
    profile with address and order history.
    """
    user = request.user
    orders = (
        Order.objects.filter(user=user, total_cost__gt=0)
        .prefetch_related('items__product')
    )
    latest_order = orders.order_by(
        '-date_created'
    ).first() if orders.exists() else None

    user_profile, created = UserProfile.objects.get_or_create(user=user)
    addresses = Address.objects.filter(user=user)
    unique_addresses = get_unique_addresses(addresses)

    context = {
        'user': user,
        'addresses': unique_addresses,
        'orders': orders,
        'latest_order': latest_order,
    }
    return render(request, 'user_profile/profile.html', context)


@login_required
def edit_profile(request):
    """
    Edit Profile View: Allow the user to edit their profile information.
    """
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Your profile was updated successfully!')
        return redirect('profile')

    context = {
        'user': user,
    }
    return render(request, 'user_profile/edit_profile.html', context)


@login_required
def manage_addresses(request):
    """
    Manage Addresses View: Allow the user to add, update, or delete addresses.
    """
    user = request.user

    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        if address_id:
            address = Address.objects.get(id=address_id, user=user)
        else:
            address = Address(user=user)

        address_fields = [
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'postcode',
            'country'
        ]
        for field in address_fields:
            value = request.POST.get(field, '')
            if field == 'country' and value == '':
                value = None
            setattr(address, field, value or None)
        if not address.street_address2:
            address.street_address2 = None
        address.save()
        messages.success(request, 'Address updated successfully!')
        return redirect('manage_addresses')

    addresses = Address.objects.filter(user=user)

    context = {
        'addresses': addresses,
        'countries': countries
    }
    return render(request, 'user_profile/manage_addresses.html', context)


@login_required
def edit_address(request, address_id):
    """
    Edit Address View: Allow the user to edit an existing address.
    """
    user = request.user
    address = get_object_or_404(Address, id=address_id, user=user)

    if request.method == 'POST':
        address_fields = [
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'postcode',
            'country'
        ]
        for field in address_fields:
            value = request.POST.get(field, '')
            if field == 'country' and value == '':
                value = None
            setattr(address, field, value or None)
        address.save()
        messages.success(request, 'Address updated successfully!')
        return redirect('manage_addresses')

    context = {
        'address': address,
        'countries': countries
    }
    return render(request, 'user_profile/edit_address.html', context)


@login_required
def delete_address(request, address_id):
    """
    Delete Address View: Allow the user to delete an existing address.
    """
    user = request.user
    address = get_object_or_404(Address, id=address_id, user=user)
    address.delete()
    messages.success(request, 'Address deleted successfully!')
    return redirect('manage_addresses')


@login_required
def delete_account(request):
    """
    Delete Account View: Delete the user's account.
    """
    user = request.user
    user.delete()
    return redirect('home')


@login_required
def confirm_delete_account(request):
    """
    Confirm Delete Account View: Display a confirmation
    page before deleting the account.
    """
    return render(request, 'user_profile/confirm_delete_account.html')
