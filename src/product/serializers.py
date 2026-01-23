from rest_framework import serializers
from .models import ProductModel


class ProductSerializer(serializers.HyperlinkedModelSerializer): # type: ignore

    class Meta: # type: ignore
        model = ProductModel
        fields = ["id", "name", "price", "description", "stock", "image"]
