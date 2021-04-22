from rest_framework import generics, permissions, viewsets
from .models import InternshipPost
from .serializers import InternshipPostSerializer

class InternshipPostViewSet(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipPostSerializer

   