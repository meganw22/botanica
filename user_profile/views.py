from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from checkout.models import Order


@login_required
def profile(request):
    """
    User Profile View: Display the user's profile with order history.
    """
    user = request.user
    orders = (
        Order.objects.filter(user=user, total_cost__gt=0)
        .prefetch_related('items__product')
    )
    latest_order = orders.order_by(
        '-date_created'
        ).first() if orders.exists() else None

    context = {
        'user': user,
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

        address = user_profile.default_address
        if not address:
            address = Address.objects.create()
            user_profile.default_address = address
            user_profile.save()

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
            setattr(address, field, request.POST.get(field, '') or None)
        address.save()

        return redirect('profile')

    context = {
        'user_profile': user_profile,
        'address': user_profile.default_address,
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
