from typing import Any
import re
from django import forms
from .models import UserRegistrationModel

labels = {
    "username" : "Ingresa tu nombre de usuario",
    "password" : "Ingresa tu contraseña",
    "email" : "Ingresa tu correo electrónico",
}


class UserRegistrationModelForm(forms.ModelForm): #type: ignore
    class Meta:
        model = UserRegistrationModel
        fields = [
            "username",
            "password",
            "email"
        ]
        exclude = []
    
    def clean_username(self, *args: Any, **kargs: Any) -> str:
        username= self.cleaned_data.get("username")
        if username is None or len(username)<5:
            raise forms.ValidationError("El nombre de usuario no puede estar vacio y debe tener al menos 5 caracteres")
        return username
    
    def clean_password(self, *args: Any, **kargs: Any) -> str:
        password= self.cleaned_data.get("password")
        if password is None or len(password)<8 or not re.search(r"[a-zA-Z]", password) or not re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
            raise forms.ValidationError("La contraseña no puede estar vacia y debe tener al menos 8 caracteres, incluir letras y caracteres especiales")
        return password
    
    def clean_email(self, *args: Any, **kargs: Any) -> str:
        email= self.cleaned_data.get("email")
        if email is None or not re.search(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("El correo electrónico no puede estar vacio y debe tener una estructura válida")
        return email