from rest_framework import generics, permissions, viewsets
from .models import OrganizationProfile
from .serializers import OrganizationProfileSerializer

class OrganizationProfileViewSet(viewsets.ModelViewSet):
    queryset = OrganizationProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrganizationProfileSerializer

   