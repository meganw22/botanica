from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Address
from checkout.models import Order

""" User Profile View """
@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(email_address=user.email).prefetch_related('items__product')
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
    address = user_profile.default_address

    if request.method == 'POST':
        # Update user details
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()

        # Update address details
        address.phone_number = request.POST.get('phone_number', '')
        address.street_address1 = request.POST.get('street_address1', '')
        address.street_address2 = request.POST.get('street_address2', '')
        address.town_or_city = request.POST.get('town_or_city', '')
        address.county = request.POST.get('county', '')
        address.postcode = request.POST.get('postcode', '')
        address.country = request.POST.get('country', '')
        address.save()

        user_profile.default_address = address
        user_profile.save()

        return redirect('profile')

    context = {
        'user_profile': user_profile,
        'address': address,
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