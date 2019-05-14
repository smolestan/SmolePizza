from django.db import models
from products.models import *

# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=64)
    price = models.DecimalField(default="0.00", max_digits=6, decimal_places=2)
    line_total = models.DecimalField(default="0.00", max_digits=6, decimal_places=2)
    topping1 = models.CharField(max_length=64, null=True, blank=True)
    topping2 = models.CharField(max_length=64, null=True, blank=True)
    topping3 = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return f"{self.product.kind} {self.product.variation} {self.product.size}"

class Cart(models.Model):
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart id: %s" %(self.id)