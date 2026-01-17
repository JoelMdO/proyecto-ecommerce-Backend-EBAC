from django.db import models
from product.models import ProductModel
from django.contrib.auth.models import User
# Create your models here.

class CartModel(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 products = models.ManyToManyField(ProductModel) #type: ignore