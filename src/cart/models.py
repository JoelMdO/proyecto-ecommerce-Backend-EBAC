from django.db import models
from product.models import ProductModel
# Create your models here.

class CartModel(models.Model):
 products = models.ManyToManyField(ProductModel) #type: ignore