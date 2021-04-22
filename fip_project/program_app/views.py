from rest_framework import generics, permissions, viewsets
from .models import Program
from .serializers import ProgramSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProgramSerializer

   