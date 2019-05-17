from django.db import models

# Create your models here.

class Kind(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(default="cheese.png", upload_to='kind_pics')

    def __str__(self):
        return f"{self.title}"

class Variation(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"

class Product(models.Model):
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    price_small = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price_large = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    price = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    image1 = models.ImageField(default="cheese.png", upload_to='product_pics')
    image2 = models.ImageField(default="regular.png", upload_to='product_pics')
    image3 = models.ImageField(default="sicilian.png", upload_to='product_pics')

    
    def __str__(self):
        return f"{self.kind} {self.variation}"

class Topping(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"