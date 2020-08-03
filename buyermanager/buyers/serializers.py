from rest_framework import serializers
from .models import Buyer


# Lead Serializer
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
