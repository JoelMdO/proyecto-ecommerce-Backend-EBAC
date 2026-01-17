from django.db import models
from cart.models import CartModel
# Create your models here.

class OrderManagerModel(models.Model):
 cart = models.OneToOneField(CartModel, on_delete=models.CASCADE)
 total = models.DecimalField(max_digits=10, decimal_places=2)
 created_at = models.DateTimeField(auto_now_add=True)