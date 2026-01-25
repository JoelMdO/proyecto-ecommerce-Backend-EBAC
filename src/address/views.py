from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import AddressModel
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated

class AddressAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request: Request):
        try:
            address = AddressModel.objects.filter(user_name=request.user.get_username())
            serializer = AddressSerializer(address, many=True, context={"request": request})  # type: ignore
            return Response(serializer.data)  # type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request):
        try:
            serializer = AddressSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)# type: ignore
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)