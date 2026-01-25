from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import CartModel
from .serializers import CartManagerSerializer

class CartAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request: Request):
        try:
            cart = CartModel.objects.filter(user_id=request.user_id)
            serializer = CartManagerSerializer(cart, many=True, context={"request": request})  # type: ignore
            return Response(serializer.data)  # type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request):
        try:
            serializer = CartManagerSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)# type: ignore
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)