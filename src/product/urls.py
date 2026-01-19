from django.urls import path

from product.views import ProductsAPIView

urlpatterns = [
path("", ProductsAPIView.as_view())
]