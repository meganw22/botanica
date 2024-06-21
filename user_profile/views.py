from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from checkout.models import Order

""" User Profile View """
@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user, total_cost__gt=0).prefetch_related('items__product')
    latest_order = orders.order_by('-date_created').first() if orders.exists() else None

    context = {
        'user': user,
        'orders': orders,
        'latest_order': latest_order,
    }

    return render(request, 'user_profile/profile.html', context)

"""Edit Profile"""
@login_required
def edit_profile(request):
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

        address.phone_number = request.POST.get('phone_number', '') or None
        address.street_address1 = request.POST.get('street_address1', '') or None
        address.street_address2 = request.POST.get('street_address2', '') or None
        address.town_or_city = request.POST.get('town_or_city', '') or None
        address.county = request.POST.get('county', '') or None
        address.postcode = request.POST.get('postcode', '') or None
        address.country = request.POST.get('country', '') or None
        address.save()

        return redirect('profile')

    context = {
        'user_profile': user_profile,
        'address': user_profile.default_address,
    }
    return render(request, 'user_profile/editprofile.html', context)

"""Delete Account"""
@login_required
def delete_account(request):
    user = request.user
    user.delete()
    return redirect('home')

@login_required
def confirm_delete_account(request):
    return render(request, 'user_profile/confirm_delete_account.html')