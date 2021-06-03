from rest_framework import permissions, viewsets
from .serializers import PersonalInformationSerializer
from .models import PersonalInformation

class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PersonalInformationSerializer
