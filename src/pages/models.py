from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)