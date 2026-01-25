from typing import List, Union
from django.urls import path, URLPattern, URLResolver
from .views import AddressAPIView


urlpatterns: List[Union[URLPattern, URLResolver]] = [
path("", AddressAPIView.as_view()),
]