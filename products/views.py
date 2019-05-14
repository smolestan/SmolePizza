from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

@login_required
def index(request):

    context = {
        "user": request.user,
        "kinds": Kind.objects.all(),
    }
    return render(request, "products/index.html", context)

@login_required
def kind_view(request, slug):

    context = {
        "user": request.user,
        "kind": Kind.objects.get(slug=slug),
        "products": Product.objects.all(),
    }
    return render(request, "products/kinds.html", context)

@login_required
def single_view(request, id):

    context = {
        "user": request.user,
        "product": Product.objects.get(id=id),

        "OneTop": Variation.objects.get(title="One topping"),
        "TwoTop": Variation.objects.get(title="Two toppings"),
        "ThreeTop": Variation.objects.get(title="Three toppings"),
        "toppings": Topping.objects.all()
    }
    return render(request, "products/single.html", context)