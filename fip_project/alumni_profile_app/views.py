from rest_framework import generics, permissions, viewsets
from .models import AlumniProfile, AlumniProfession
from .serializers import AlumniProfileSerializer, AlumniProfessionSerializer

class AlumniProfileViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AlumniProfileSerializer


class AlumniProfessionViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AlumniProfessionSerializer

   