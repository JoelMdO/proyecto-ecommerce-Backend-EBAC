from .views import FormsView
from django.urls import path

urlpatterns = [
    path("", FormsView.as_view(), name="forms")
]