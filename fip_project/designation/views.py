from rest_framework import generics, permissions, viewsets
from .models import Designation
from .serializers import DesignationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DesignationSerializer

   