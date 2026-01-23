from django.contrib import admin
from .models import ProductModel
# Register your models here.
class ProductAdmin(admin.ModelAdmin): #type: ignore
    list_display = ('id', 'name', 'price', 'stock', 'image')  # type: ignore
    search_fields = ('name',)  # type: ignore

admin.site.register(ProductModel, ProductAdmin)  # type: ignore