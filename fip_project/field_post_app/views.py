from rest_framework import generics, permissions, viewsets
from .models import FieldPost
from .serializers import FieldPostSerializer

class FieldPostViewSet(viewsets.ModelViewSet):
    queryset = FieldPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldPostSerializer

   