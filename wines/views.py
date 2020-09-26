from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Wine, Category, Grape

# Create your views here.

def all_wines(request):
    """ A view to show all wines, including sorting and search queries """

    wines = Wine.objects.all()
    query = None
    category = None
    grape = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                wines = wines.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            wines = wines.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET.get('category','')
            wines = wines.filter(category__name=category)

        if 'grape' in request.GET:
            grape = request.GET.get('grape','')
            wines = wines.filter(grape__name=grape)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('wines'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query) | Q(grape__name__icontains=query)
            wines = wines.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wines': wines,
        'search_term': query,
        'current_category': category,
        'current_grape': grape,
        'current_sorting': current_sorting,
    }

    return render(request, 'wines/wines.html', context)


def wine_detail(request, wine_id):
    """ A view to show individual product details """

    wine = get_object_or_404(Wine, pk=wine_id)

    context = {
        'wine': wine,
    }

    return render(request, 'wines/wine_detail.html', context)