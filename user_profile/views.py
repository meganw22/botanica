from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import Order
from checkout.forms import AddressForm

@login_required
def profile(request):
    orders = Order.objects.filter(email_address=request.user.email)
    return render(request, 'user_profile/profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    user = request.user
    latest_order = Order.objects.filter(email_address=user.email).order_by('-date_created').first()

    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=latest_order)
        if address_form.is_valid():
            address_form.save()
            
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            
            return redirect('profile')
    else:
        address_form = AddressForm(instance=latest_order)

    context = {
        'latest_order': latest_order,
        'address_form': address_form,
    }
    return render(request, 'user_profile/editprofile.html', context)
