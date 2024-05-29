from django.shortcuts import render

# Create your views here.
def shopping_bag(request):
    context = {
        'bag': request.session.get('bag', [])
    }
    return render(request, 'bag/bag.html', context)