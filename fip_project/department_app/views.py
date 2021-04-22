from rest_framework import generics, permissions, viewsets
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DepartmentSerializer

   