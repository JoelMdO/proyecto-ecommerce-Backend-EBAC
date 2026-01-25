from rest_framework import serializers
from .models import AddressModel


class AddressSerializer(serializers.HyperlinkedModelSerializer): # type: ignore

    class Meta: # type: ignore
        model = AddressModel
        fields = ["id", "user_name", "address", "card", "phone"]