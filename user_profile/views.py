from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import Order

""" User Profile View """
@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(email_address=user.email)
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
    latest_order = Order.objects.filter(email_address=user.email).order_by('-date_created').first()

    if request.method == 'POST':
        # Update user details
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()

        # Update latest order address details
        if latest_order:
            latest_order.address_line1 = request.POST.get('address_line1', '')
            latest_order.address_line2 = request.POST.get('address_line2', '')
            latest_order.city = request.POST.get('city', '')
            latest_order.county = request.POST.get('county', '')
            latest_order.postcode = request.POST.get('postcode', '')
            latest_order.country = request.POST.get('country', '')
            latest_order.save()

        return redirect('profile')

    context = {
        'latest_order': latest_order,
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