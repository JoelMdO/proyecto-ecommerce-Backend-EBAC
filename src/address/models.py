from django.db import models

# Create your models here.
class AddressModel(models.Model):
 user_name = models.CharField(max_length=255) # type: ignore
 address = models.CharField(max_length=100)# type: ignore
 card = models.CharField(max_length=16)# type: ignore
 phone = models.CharField(max_length=15) # type: ignore
