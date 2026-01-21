from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=150)  # type: ignore[reportUnknownVariableType]
    email = models.EmailField() # type: ignore
    password = models.CharField(max_length=128) # type: ignore