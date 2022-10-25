from django.shortcuts import render
from .models import Favorite
# Create your views here.


def favorites(request):
    """ Display the favorites page. """

    favorite_products = Favorite.objects.all()

    template = 'favorites/favorites.html'
    context = {
        'favorite_products': favorite_products,
    }

    return render(request, template, context)