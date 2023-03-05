from django.shortcuts import render

# Create your views here.


def bouquet_detail(request): 
    """ A view to return the index page """
    return render(request, 'create_a_bouquet/bouquet_detail.html')
