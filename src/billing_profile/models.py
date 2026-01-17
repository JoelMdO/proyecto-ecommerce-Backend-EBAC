from django.db import models
from django.contrib.auth.models import User
from address.models import AddressModel

# Create your models here.
class BillingProfileModel(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 address = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
 card = models.CharField(max_length=16)
 expiration_date = models.DateField()
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)