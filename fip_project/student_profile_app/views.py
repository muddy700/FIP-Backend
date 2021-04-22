from rest_framework import generics, permissions, viewsets
from .models import StudentProfile, StudentProfession
from .serializers import StudentProfileSerializer, StudentProfessionSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StudentProfileSerializer

   

class StudentProfessionViewSet(viewsets.ModelViewSet):
    queryset = StudentProfession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StudentProfessionSerializer

   