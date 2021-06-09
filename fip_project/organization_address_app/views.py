from rest_framework import generics, permissions, viewsets
from .models import Invitations, OrganizationProfile, Contract, Rating
from .serializers import InvitationsSerializer, OrganizationProfileSerializer, ContractSerializer, RatingSerializer

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
class InvitationsViewSet(viewsets.ModelViewSet):
    queryset = Invitations.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InvitationsSerializer

   