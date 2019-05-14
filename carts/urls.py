from django.urls import path

from . import views

urlpatterns = [
    path("cart", views.view, name="cart"),
    path('cart/<int:id>/', views.update_cart, name='update_cart'),
]
