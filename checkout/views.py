from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('wines'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HK2xuDcAlhOsXkbkSFboZCWum9c0G6yjimHr6fVseSKLDKFAEBPpgtFVdj026fiugWbWdk1J0mP2pNKk2pF1xZq00PuBOV59a',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)