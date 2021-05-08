from rest_framework import generics, permissions, viewsets
from .models import ( InternshipPost, InternshipApplication )
from .serializers import (InternshipPostSerializer, 
 InternshipApplicationSerializer )

class InternshipPostViewSet(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipPostSerializer

class InternshipApplicationViewSet(viewsets.ModelViewSet):
    queryset = InternshipApplication.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipApplicationSerializer

   