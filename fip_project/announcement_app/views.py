from rest_framework import generics, permissions, viewsets
from .models import Announcement
from .serializers import AnnouncementSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = AnnouncementSerializer

   