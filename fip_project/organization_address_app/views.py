from rest_framework import generics, permissions, viewsets
from .models import Invitations, OrganizationProfile, Contract, Rating, Notification, NotificationView
from .serializers import InvitationsSerializer, NotificationViewsSerializer, OrganizationProfileSerializer, ContractSerializer, RatingSerializer, NotificationsSerializer, __name__

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

   
class NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = NotificationsSerializer

   
class NotificationViewsViewSet(viewsets.ModelViewSet):
    queryset = NotificationView.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = NotificationViewsSerializer

   