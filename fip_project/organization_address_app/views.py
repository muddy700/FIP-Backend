from rest_framework import generics, permissions, viewsets
from .models import OrganizationProfile, Contract, Rating
from .serializers import OrganizationProfileSerializer, ContractSerializer, RatingSerializer

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

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = RatingSerializer

   