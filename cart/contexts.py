def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'bag_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
