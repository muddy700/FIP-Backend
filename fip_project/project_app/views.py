from rest_framework import generics, permissions, viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProjectSerializer

   