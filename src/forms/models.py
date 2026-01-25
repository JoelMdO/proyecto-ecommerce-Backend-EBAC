from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class UserRegistrationModel(models.Model):
    username = models.CharField(max_length=150, validators=[MinLengthValidator(5)]) #type: ignore
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)]) #type: ignore
    email = models.EmailField() #type: ignore