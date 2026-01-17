from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)