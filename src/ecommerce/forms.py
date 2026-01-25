from django import forms
from django.contrib.auth.models import User
# from .models import Product  # Uncomment and define your Product model

class UserRegistrationForm(forms.ModelForm): #type: ignore
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password") #type: ignore
        password_confirm = cleaned_data.get("password_confirm") #type: ignore
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data

# Example ProductForm (assuming you have a Product model)
class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)
