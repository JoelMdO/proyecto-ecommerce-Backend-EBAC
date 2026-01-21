from typing import List, Union
from django.urls import include, path, URLPattern, URLResolver
from product.views import ProductsAPIView, ProductsPaginationListAPIView, ProductsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product-viewset", ProductsViewSet, basename="product-viewset")


urlpatterns: List[Union[URLPattern, URLResolver]] = [
path("", ProductsAPIView.as_view()),
path("viewsets/", include(router.urls)),
path("pagination/", ProductsPaginationListAPIView.as_view()),
]