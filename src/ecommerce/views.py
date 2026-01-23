import os
from django import get_version
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView


def home(request: HttpRequest):
    context: Dict[str, Any] = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)

# Authentication views were moved to the `user` app to improve separation of concerns

# Products List View
class ProductsListView(ListView): # type: ignore
    template_name = "products/product_list.html"
    # model = Product  # Define your Product model
    context_object_name = "products"

# Product Detail View
class ProductDetailView(DetailView): # type: ignore
    template_name = "products/product_detail.html"
    # model = Product
    context_object_name = "product"

# Shopping Cart - Added Products
class ShopCartAddedProductsView(LoginRequiredMixin, TemplateView):
    template_name = "cart/cart_products.html"

# Checkout Products
class CheckoutProductsView(LoginRequiredMixin, TemplateView):
    template_name = "checkout/checkout_products.html"

# Checkout User Address
class CheckoutUserAddressView(LoginRequiredMixin, TemplateView):
    template_name = "checkout/checkout_address.html"

# Checkout Credit Card Information
class CheckoutCreditCardView(LoginRequiredMixin, TemplateView):
    template_name = "checkout/checkout_credit_card.html"

# Chart AjaxView 
class SalesAjaxDashboardView(TemplateView):
    template_name = "sales/chart.html"

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = "sales/sales.html"
