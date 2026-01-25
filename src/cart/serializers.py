from rest_framework import serializers
from .models import CartModel


class CartManagerSerializer(serializers.HyperlinkedModelSerializer): # type: ignore

    class Meta: # type: ignore
        model = CartModel
        fields = ["alt", "id", "image", "name", "price"]