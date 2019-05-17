from django.apps import AppConfig
import vinaigrette

class ProductsConfig(AppConfig):
    name = 'products'
    
    def ready(self):
        from .models import Kind, Variation, Topping
        Kind = self.get_model("Kind")
        Variation = self.get_model("Variation")
        Topping = self.get_model("Topping")
        vinaigrette.register(Kind, ['title', 'description'])
        vinaigrette.register(Variation, ['title', 'description'])
        vinaigrette.register(Topping, ['title'])