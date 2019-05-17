from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your views here.

from products.models import Product

from .models import Cart, CartItem

@login_required
def view(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        empty_message = _("Your Cart is Empty")
        context = {"empty": True, "empty_message": empty_message}

    return render(request, "carts/view.html", context)

@login_required
def update_cart(request, id):
    
    if request.method == "POST":
        try:
            qty = request.POST['qty']
        except:
            qty = None
        try:
            toppings = request.POST.getlist('toppings')
        except:
            toppings = None
        try:
            rem = request.POST['rem']
        except:
            rem = False

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        pass

    if rem:
        CartItem.objects.filter(id=rem).delete()

    if qty:
        cart_item = CartItem(cart=cart, product=product, quantity=qty)
        try:
            cart_item.topping1 = toppings[0]
            cart_item.topping2 = toppings[1]
            cart_item.topping3 = toppings[2]
        except:
            pass
        size = request.POST['size']
        cart_item.size = size
        if size == "-":
            cart_item.price = product.price
            cart_item.line_total = float(product.price) * int(qty)
        elif size == "large":
            cart_item.price = product.price_large
            cart_item.line_total = float(product.price_large) * int(qty)
        elif size == "small":
            cart_item.price = product.price_small
            cart_item.line_total = float(product.price_small) * int(qty)
        cart_item.save()

    new_total = 0.00
    for item in cart.cartitem_set.all():

        line_total = float(item.price) * item.quantity
        new_total += line_total

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    
    return HttpResponseRedirect(reverse("cart"))