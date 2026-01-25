from django.db import models
from django.contrib.auth.models import User
from address.models import AddressModel

# Create your models here.
class BillingProfileModel(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE) # type: ignore
 address = models.ForeignKey(AddressModel, on_delete=models.CASCADE) # type: ignore
 card = models.CharField(max_length=16) # type: ignore
 expiration_date = models.DateField() # type: ignore
 created_at = models.DateTimeField(auto_now_add=True) # type: ignore
 updated_at = models.DateTimeField(auto_now=True) # type: ignore