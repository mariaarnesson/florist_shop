from django.shortcuts import render

# Create your views here.


def bouquet(request): 
    """ A view to return the index page """
    return render(request, 'create_a_bouquet/bouquet.html')

