from django.urls import path

from . import views

urlpatterns = [
    path("checkout", views.checkout, name="checkout"),
    path("orders", views.orders, name="user_orders"),
    path("all-orders", views.all_orders, name="all_orders"),

]