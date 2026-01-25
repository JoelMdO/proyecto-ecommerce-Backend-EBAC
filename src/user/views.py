# Create your views here.
from typing import Any
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from user.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView, PasswordResetView
from django.urls import reverse_lazy


@api_view(['POST', ])
def registration_view(request: Request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account: Any = serializer.save()

            data["response"] = "Registro Exitoso"
            data["username"] = account.username

            jwt_tokens = RefreshToken.for_user(account)
            data["token"] = {
                "refresh": str(jwt_tokens),
                "access": str(jwt_tokens.access_token)
            }

        else:
            data = serializer.errors  # type: ignore

    return Response(data)  # type: ignore


class LoginView(APIView):
    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            jwt_tokens = RefreshToken.for_user(user)
            data = { # type: ignore
                'username': user.username, # type: ignore
                'token': {
                    'refresh': str(jwt_tokens),
                    'access': str(jwt_tokens.access_token),
                }
            }
            return Response(data)
        return Response({'error': 'Credenciales inválidas'}, status=400)


class LogoutUserView(APIView):
    """Blacklist a given refresh token (client must POST the refresh token)."""
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token required"}, status=400)
        try:
            RefreshToken(refresh_token).blacklist()
            return Response(status=204)
        except Exception:
            return Response({"detail": "Invalid or already blacklisted token"}, status=400)


class UserRegistrationView(TemplateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(DjangoLoginView):
    template_name = "registration/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login") # type: ignore


class UserPasswordResetView(PasswordResetView):
    template_name = "registration/password_reset.html"
    email_template_name = "registration/password_reset_email.html"
    success_url = reverse_lazy("login")