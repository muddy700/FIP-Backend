from rest_framework import generics, permissions, viewsets
from .models import Profession
from .serializers import ProfessionSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ProfessionSerializer

   