from django.shortcuts import render

# Create your views here.
def all_products(request):
    """ All product views to display all plants and products """
    
    return render(request, 'products/products.html')