from rest_framework import generics, permissions, viewsets
from .models import StaffProfile
from .serializers import StaffProfileSerializer

class StaffProfileViewSet(viewsets.ModelViewSet):
    queryset = StaffProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StaffProfileSerializer

   