from typing import List, Union
from django.urls import path, URLPattern, URLResolver
from .views import CartAPIView


urlpatterns: List[Union[URLPattern, URLResolver]] = [
path("", CartAPIView.as_view()),
]