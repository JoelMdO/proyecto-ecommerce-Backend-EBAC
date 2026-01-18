from django.urls import path

from ecommerce import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("password-reset/", views.UserPasswordResetView.as_view(), name="password_reset"),
    path("products/", views.ProductsListView.as_view(), name="product_list"),
    path("products/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("cart/", views.ShopCartAddedProductsView.as_view(), name="cart_products"),
    path("checkout/products/", views.CheckoutProductsView.as_view(), name="checkout_products"),
    path("checkout/address/", views.CheckoutUserAddressView.as_view(), name="checkout_address"),
    path("checkout/credit-card/", views.CheckoutCreditCardView.as_view(), name="checkout_credit_card"),
]
