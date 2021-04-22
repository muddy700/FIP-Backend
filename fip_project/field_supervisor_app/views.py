from rest_framework import generics, permissions, viewsets
from .models import FieldSupervisorProfile
from .serializers import FieldSupervisorProfileSerializer

class FieldSupervisorProfileViewSet(viewsets.ModelViewSet):
    queryset = FieldSupervisorProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldSupervisorProfileSerializer

   