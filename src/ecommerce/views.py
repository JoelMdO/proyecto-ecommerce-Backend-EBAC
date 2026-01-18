import os
from django import get_version
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy

def home(request: HttpRequest):
    context: Dict[str, Any] = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)

# User Registration View
class UserRegistrationView(TemplateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    # form_class = UserRegistrationForm  # Define this form in your forms.py

# User Login View
class UserLoginView(LoginView):
    template_name = "registration/login.html"

# User Logout View
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")

# Password Reset View
class UserPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset.html"
    email_template_name = "registration/password_reset_email.html"
    success_url = reverse_lazy("login")

# Products List View
class ProductsListView(ListView):
    template_name = "products/product_list.html"
    # model = Product  # Define your Product model
    context_object_name = "products"

# Product Detail View
class ProductDetailView(DetailView):
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
