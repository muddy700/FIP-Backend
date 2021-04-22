from rest_framework import generics, permissions, viewsets
from .models import OrganizationAddress
from .serializers import OrganizationAddressSerializer

class OrganizationAddressViewSet(viewsets.ModelViewSet):
    queryset = OrganizationAddress.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrganizationAddressSerializer

   