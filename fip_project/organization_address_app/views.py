from rest_framework import generics, permissions, viewsets
from .models import OrganizationProfile, Contract
from .serializers import OrganizationProfileSerializer, ContractSerializer

class OrganizationProfileViewSet(viewsets.ModelViewSet):
    queryset = OrganizationProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrganizationProfileSerializer

   
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ContractSerializer

   