from django.db import models

# Create your models here.
from carts.models import Cart
from django.contrib.auth.models import User

class Status(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    order_id = models.CharField(max_length=64, default='ABC', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id