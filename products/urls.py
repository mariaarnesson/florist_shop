from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path(
        'add_favourite/<int:product_id>/',
        views.add_favourite, name='add_favourite'),
    path(
        'remove_favourite/<int:product_id>/',
        views.remove_favourite, name='remove_favourite'),
    path(
        'favourite_list/',
        views.favourite_list, name='favourite_list'),
    # path(
    #    'toggle_fav/<int:product_id>/',
    #   views.toggle_favourite,
    #    name='toggle_favourite'),  
]
