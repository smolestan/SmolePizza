from django.apps import AppConfig
import vinaigrette


class CartsConfig(AppConfig):
    name = 'carts'

    def ready(self):
        from .models import CartItem
        CartItem = self.get_model("CartItem")
        vinaigrette.register(CartItem, ['size'])
