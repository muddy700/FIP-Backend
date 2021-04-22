from rest_framework import generics, permissions, viewsets
from .models import Certificate
from .serializers import CertificateSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CertificateSerializer

   