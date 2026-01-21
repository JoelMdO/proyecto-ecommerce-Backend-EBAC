# Create your views here.
from typing import Any
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from user.serializers import RegistrationSerializer

@api_view(['POST', ]) 
def registration_view(request: Request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data = request.data)

        data = {}

        if serializer.is_valid():
            account: Any = serializer.save()

            data["response"] = "Registro Exitoso"
            data["username"] = account.username
            data["email"] = account.email

            jwt_tokens = RefreshToken.for_user(account)
            data["token"] = {
                "refresh": str(jwt_tokens),
                "access": str(jwt_tokens.access_token)
            }

        else:
            data = serializer.errors #type: ignore

    return Response(data) # type: ignore
    

class LoginView(APIView):
    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token_created = Token.objects.get_or_create(user=user)
            return Response({'token': token_created})
        return Response({'error': 'Credenciales inválidas'}, status=400)