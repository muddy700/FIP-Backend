from rest_framework import generics, permissions, viewsets
from .models import Organization
from .serializers import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrganizationSerializer

   