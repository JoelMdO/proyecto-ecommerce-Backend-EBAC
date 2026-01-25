from django.contrib import admin
from .models import CartModel


class CartModelAdmin(admin.ModelAdmin): # type: ignore
    list_display = ("id", "product_count", "products_list")
    readonly_fields = ("products_list",)
    filter_horizontal = ("products",)

    def products_list(self, obj): # type: ignore
        return ", ".join([getattr(p, "name", str(p.pk)) for p in obj.products.all()]) # type: ignore
    products_list.short_description = "Selected products" # type: ignore

    def product_count(self, obj): # type: ignore
        return obj.products.count() # type: ignore
    product_count.short_description = "Products" # type: ignore


admin.site.register(CartModel, CartModelAdmin) # type: ignore
