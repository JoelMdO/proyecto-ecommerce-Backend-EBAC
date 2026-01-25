from rest_framework import serializers
from .models import OrderManagerModel
from cart.models import CartModel


class OrderManagerSerializer(serializers.ModelSerializer): # type: ignore
    # accept cart as primary key (frontend sends an integer id)
    cart = serializers.PrimaryKeyRelatedField(queryset=CartModel.objects.all()) # type: ignore
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta: # type: ignore
        model = OrderManagerModel
        fields = ["id", "user_name", "cart", "total", "created_at"]
