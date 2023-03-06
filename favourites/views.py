from django.shortcuts import render
from .models import Product, Category


# Create your views here.


def all_favourites(request): 
    """ A view to return the index page """
    return render(request, 'favourites/all_favourites.html')
