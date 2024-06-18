from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order

@login_required
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You've got nothing in your bag at the moment!")
        return redirect(reverse('products'))

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.email_address = request.user.email

            # Save the order and redirect to profile
            order.save()
            messages.success(request, "Order placed successfully!")
            return redirect('profile')
        else:
            messages.error(request, "There was an error with your form. Please check your information.")
    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PCPIDP6pKOKWMhIjtkTCCut8jXd4IxvtooBMGkXTCfcKoqsfkxrcsikSpn9PKuqyGqcFOZb9je0VWfMDfwYkMuf00OuzHstIA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
