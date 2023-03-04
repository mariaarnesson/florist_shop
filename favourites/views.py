from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def all_favourites(request): 
    """ A view to return the index page """
    return render(request, 'favourites/all_favourites.html')