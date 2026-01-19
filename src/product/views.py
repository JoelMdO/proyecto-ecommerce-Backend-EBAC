from typing import Any
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import ProductModel
from .serializers import ProductSerializer


# List products (price > 1000) and create new products
class ProductsAPIView(APIView):
    def get(self, request: Request):
        try:
            products = ProductModel.objects.filter(price__gt=1000)
            serializer = ProductSerializer(products, many=True, context={"request": request})  # type: ignore
            return Response(serializer.data)  # type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request):
        try:
            serializer = ProductSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)# type: ignore
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request: Request, *args: Any, **kwargs: Any):
        try:
            product_to_delete = request.data.get("product_id")
            if not product_to_delete:
                return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            product = ProductModel.objects.get(id=product_to_delete)
            product.delete()
            return Response({"deleted": product_to_delete}, status=status.HTTP_200_OK)
        except ProductModel.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Partial update for a single product (e.g., update price)
class ProductDetailAPIView(APIView):
    def put(self, request: Request, pk: int):
        try:
            product = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True, context={"request": request})
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)# type: ignore
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# type: ignore
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)