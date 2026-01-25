from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import registration_view, LoginView
from user.views import LogoutUserView

urlpatterns = [
   path("login", LoginView.as_view()),
   path("register", registration_view),
   path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
   path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
   path("logout", LogoutUserView.as_view(), name="token_blacklist_logout"),
]