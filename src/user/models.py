from django.db import models
from django.utils import timezone

class UserModel(models.Model):
    id = models.AutoField(primary_key=True) # type: ignore
    username = models.CharField(max_length=150, unique=True) # type: ignore
    email = models.EmailField(unique=True) # type: ignore
    password = models.CharField(max_length=128) # type: ignore
    date_joined = models.DateTimeField(default=timezone.now) # type: ignore

    def __str__(self) -> str:
        return self.username # type: ignore