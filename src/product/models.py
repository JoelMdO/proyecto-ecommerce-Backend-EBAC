from django.db import models
from decimal import Decimal


class ProductModel(models.Model):
    id = models.AutoField(primary_key=True) # type: ignore
    name = models.CharField(max_length=255) # type: ignore
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00')) # type: ignore
    alt = models.CharField(max_length=255) # type: ignore
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) # type: ignore
    
    def __str__(self) -> str:
        return self.name # type: ignore