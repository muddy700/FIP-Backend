from rest_framework import generics, permissions, viewsets
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StudentProfileSerializer

   