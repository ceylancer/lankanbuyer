from .models import Buyer
from rest_framework import viewsets, permissions
from .serializers import BuyerSerializer


# Buyer Viewset
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BuyerSerializer
