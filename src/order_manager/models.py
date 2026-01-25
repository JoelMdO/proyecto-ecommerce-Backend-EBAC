from django.db import models
from cart.models import CartModel
# Create your models here.

class OrderManagerModel(models.Model):
 id = models.AutoField(primary_key=True) # type: ignore
 user_name = models.CharField(max_length=255)# type: ignore
 cart = models.OneToOneField(CartModel, on_delete=models.CASCADE)# type: ignore
 total = models.DecimalField(max_digits=10, decimal_places=2)# type: ignore
 created_at = models.DateTimeField(auto_now_add=True)# type: ignore