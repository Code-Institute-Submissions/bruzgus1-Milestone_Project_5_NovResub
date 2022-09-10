from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    tier = None
    if 'product_tier' in request.POST:
        tier = request.POST['product_tier']
    cart = request.session.get('cart', {})

    if tier:
        if item_id in list(cart.keys()):
            if tier in cart[item_id]['items_by_tier'].keys():
                cart[item_id]['items_by_tier'][tier] += quantity
            else:
                cart[item_id]['items_by_tier'][tier] = quantity
        else:
            cart[item_id] = {'items_by_tier': {tier: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
