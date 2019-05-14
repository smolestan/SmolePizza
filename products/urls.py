from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('kinds/<slug:slug>/', views.kind_view, name='kinds'),
    path('products/<int:id>/', views.single_view, name='products'),
]
