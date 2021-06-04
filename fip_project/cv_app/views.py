from rest_framework import permissions, viewsets
from .serializers import PersonalInformationSerializer, EducationInformationSerializer
from .models import PersonalInformation, EducationInformation

class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PersonalInformationSerializer

class EducationInformationViewSet(viewsets.ModelViewSet):
    queryset = EducationInformation.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EducationInformationSerializer
