from django.urls import path

from ecommerce import views
from user import views as user_views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", user_views.UserRegistrationView.as_view(), name="register"),
    path("login/", user_views.UserLoginView.as_view(), name="login"),
    path("logout/", user_views.UserLogoutView.as_view(), name="logout"),
    path("password-reset/", user_views.UserPasswordResetView.as_view(), name="password_reset"),
    path("products/", views.ProductsListView.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("cart/", views.ShopCartAddedProductsView.as_view(), name="cart_products"),
    path("checkout/products/", views.CheckoutProductsView.as_view(), name="checkout_products"),
    path("checkout/address/", views.CheckoutUserAddressView.as_view(), name="checkout_address"),
    path("checkout/credit-card/", views.CheckoutCreditCardView.as_view(), name="checkout_credit_card"),
]
