from django.shortcuts import render, redirect
from products.models import Product
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')


def search(request):
    """Search views"""
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(
            Q(easy_name__icontains=query) | Q(scientific_name__icontains=query)
        )
    else:
        results = Product.objects.none()

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'home/search_results.html', context)


def newsletter_signup(request):
    """Sign up to newsletter"""
    if request.method == 'POST':
        email = request.POST.get('email')
        messages.success(
            request, 'Thank you for signing up for our newsletter!')
        return redirect('home')
    return HttpResponse(status=405)
