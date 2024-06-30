from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from checkout.models import Order
from django_countries import countries
from django.contrib import messages


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

    context = {
        'user': user,
        'addresses': addresses,
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
    user_profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()

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
        address.save()

        messages.success(request, 'Your profile was updated successfully!')
        return redirect('profile')

    addresses = Address.objects.filter(user=user)

    context = {
        'user_profile': user_profile,
        'addresses': addresses,
        'countries': countries
    }
    return render(request, 'user_profile/editprofile.html', context)


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
