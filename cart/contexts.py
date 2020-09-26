from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from wines.models import Wine

def cart_contents(request):

    cart_items = []
    total = 0
    no_of_items = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        wine = get_object_or_404(Wine, pk=item_id)
        total += quantity * wine.price
        no_of_items += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'wine': wine,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'number_of_items': no_of_items,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context