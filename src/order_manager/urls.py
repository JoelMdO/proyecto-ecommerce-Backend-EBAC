from typing import List, Union
from django.urls import path, URLPattern, URLResolver
from .views import OrdersAPIView


urlpatterns: List[Union[URLPattern, URLResolver]] = [
path("", OrdersAPIView.as_view()),
]