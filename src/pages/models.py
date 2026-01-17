from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

class UserModel(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)