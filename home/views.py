from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

# Search View
def search(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(Q(easy_name__icontains=query) | Q(height__icontains=query))
    else:
        results = Product.objects.none()

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'home/search_results.html', context)