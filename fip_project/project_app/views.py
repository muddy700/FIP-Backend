from rest_framework import generics, permissions, viewsets
from .models import Project, ProjectMember
from .serializers import ProjectSerializer, ProjectMemberSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProjectSerializer

   
class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProjectMemberSerializer

   