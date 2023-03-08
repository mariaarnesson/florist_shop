from django.urls import path
from . import views

urlpatterns = [
    path('', views.bouquet, name='creata_a_bouquet'),
]
