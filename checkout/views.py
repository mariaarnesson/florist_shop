from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MfsVlK1mRCHaetcYGfgefU76vTWLhLj7u5Qpk6T2fw5Zu5QOAbSxx1FkgypQ9y7lwid2tcjHSj3HKKbD7PUFyVt00eQ50LPUS'
         'client_secret': 'test client secret',
    }

    return render(request, template, context)