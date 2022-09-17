from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def update_cart(request, item_id):
    """Update a quantity of the specified product in the shopping cart """

    quantity = int(request.POST.get('quantity'))
    tier = None
    if 'product_tier' in request.POST:
        tier = request.POST['product_tier']
    cart = request.session.get('cart', {})

    if tier:
        if quantity > 0:
            cart[item_id]['items_by_tier'][tier] = quantity
        else:
            del cart[item_id]['items_by_tier'][tier]
            if not cart[item_id]['items_by_tier']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = Product.objects.get(pk=item_id)
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
            messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        tier = None
        if 'product_tier' in request.POST:
            tier = request.POST['product_tier']
        cart = request.session.get('cart', {})

        if tier:
            del cart[item_id]['items_by_tier'][tier]
            if not cart[item_id]['items_by_tier']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
