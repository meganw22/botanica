from django.shortcuts import render

# Create your views here.
def shopping_bag(request):
    bag = request.session.get('bag', [])
    context = {
        'bag': bag,
    }
    return render(request, 'bag/bag.html', context)