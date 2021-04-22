from rest_framework import generics, permissions, viewsets
from .models import AlumniProfile
from .serializers import AlumniProfileSerializer

class AlumniProfileViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AlumniProfileSerializer

   