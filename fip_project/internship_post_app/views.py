from rest_framework import generics, permissions, viewsets
from .models import ( InternshipPost, InternshipPostProfession,
 InternshipApplication )
from .serializers import (InternshipPostSerializer, 
 InternshipApplicationSerializer,
  InternshipPostProfessionSerializer )

class InternshipPostViewSet(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipPostSerializer

class InternshipPostProfessionViewSet(viewsets.ModelViewSet):
    queryset = InternshipPostProfession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipPostProfessionSerializer

   
class InternshipApplicationViewSet(viewsets.ModelViewSet):
    queryset = InternshipApplication.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipApplicationSerializer

   