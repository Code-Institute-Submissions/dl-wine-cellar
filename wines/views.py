from django.shortcuts import render
from .models import Wine

# Create your views here.

def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wines/wines.html', context)