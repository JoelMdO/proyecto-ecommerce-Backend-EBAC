from django.contrib import admin
from .models import ProductModel, UserModel

admin.site.register(ProductModel)
admin.site.register(UserModel)