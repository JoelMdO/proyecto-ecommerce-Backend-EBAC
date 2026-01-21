from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import registration_view

urlpatterns = [
   path("login", obtain_auth_token),
   path("register", registration_view),
   path("api/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
   path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]