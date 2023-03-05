from django.urls import path
from . import views

urlpatterns = [
    path('', views.bouquet_detail, name='creata_a_bouquet'),
]