from django.apps import AppConfig
import vinaigrette

class OrdersConfig(AppConfig):
    name = 'orders'
    
    def ready(self):
        from .models import Status
        Status = self.get_model("Status")
        vinaigrette.register(Status, ['title'])
