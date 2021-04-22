from rest_framework import generics, permissions, viewsets
from .models import FieldPost, FieldPostProfession, FieldApplication
from .serializers import FieldPostSerializer, FieldApplicationSerializer, FieldPostProfessionSerializer

class FieldPostViewSet(viewsets.ModelViewSet):
    queryset = FieldPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldPostSerializer

   
class FieldPostProfessionViewSet(viewsets.ModelViewSet):
    queryset = FieldPostProfession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldPostProfessionSerializer

   
class FieldApplicationViewSet(viewsets.ModelViewSet):
    queryset = FieldApplication.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldApplicationSerializer

   