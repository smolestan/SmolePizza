from django.contrib import admin
from .models import Product, Topping, Kind, Variation

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price_small', 'price_large', 'price']
    list_editable = ['price', 'price_large', 'price_small']

    class Meta:
        model = Product

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Topping)
admin.site.register(Kind)
admin.site.register(Variation)
