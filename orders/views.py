from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

from carts.models import Cart
from .models import Order, Status
from .utils import id_generator

@login_required
def orders(request):

    context = {
    }
    return render(request, "orders/user.html", context)

@login_required
def all_orders(request):

    statuses = Status.objects.all()
    all_orders = Order.objects.all()

    context = {
        "all_orders": all_orders,
        "statuses": statuses
    }
    
    if request.method == "POST" and request.user.is_staff:
        for statuse in statuses:
            order_to_change = request.POST.get(str(statuse))
            if order_to_change:
                order = Order.objects.get(order_id=order_to_change)
                order.status = statuse
                order.save()
                return render(request, "orders/all.html", context)
            else:
                continue
        try:
            fil = request.POST.get('filter')
            if fil == "All Orders":
                return render(request, "orders/all.html", context)
            else:
                all_orders = Order.objects.filter(status__title=fil)
                context["all_orders"] = all_orders
                context["fil"] = fil
                return render(request, "orders/all.html", context)
        except:
            return render(request, "orders/all.html", context)
    elif request.user.is_staff:
        return render(request, "orders/all.html", context)
    else:
        return render(request, "orders/user.html", context)

@login_required
def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        new_order = Order.objects.get(cart=cart, user=request.user)
    except Order.DoesNotExist:
        new_order = Order(cart=cart, user=request.user, status=Status.objects.get(title="Pending"))
        new_order.order_id = id_generator()
        new_order.save()
        del request.session['cart_id']
        del request.session['items_total']
        # send_mail("Order created", "Hi! Your order has been created successfully", "smolestan@gmail.com", ["smolestan@gmail.com"], fail_silently=False)
        return HttpResponseRedirect(reverse("user_orders"))

    context = {
        "user": request.user,
    }
    return render(request, "products/index.html", context)