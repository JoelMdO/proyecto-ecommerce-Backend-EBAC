from typing import Any
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError, CharField

class RegistrationSerializer(ModelSerializer[User]):
    password2 = CharField(style={
        "input_type":"password"}, 
        write_only=True
        )
    
    class Meta(): # type: ignore 
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password" : {"write_only": True}
        }
    
    def save(self, **kwargs: Any):
        password = self.validated_data.get("password")
        password2 = self.validated_data.get("password2")

        if password != password2:
            raise ValidationError({"error":"password y password2 deben ser iguales"})
        
        email = self.validated_data.get("email")

        if User.objects.filter(email=email).exists():
            raise ValidationError({"error": "Ese correo ya esta registrado"})
        
        username = self.validated_data.get("username")

        account = User(email=email, username=username)
        account.set_password(password)
        account.save()

        return account

class UserSerializer(ModelSerializer[User]):
    class Meta(): # type: ignore 
        model = User
        fields = ["id", "username", "email"]