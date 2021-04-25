from rest_framework import generics, permissions
from .models import StudentProfile, StudentProfession
from .serializers import StudentProfileSerializer, StudentProfessionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets, mixins

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StudentProfileSerializer

class StudentsProfessionsViewSet(viewsets.ModelViewSet):
    queryset = StudentProfession.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = StudentProfessionSerializer

class StudentProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfessionSerializer
    queryset = StudentProfession.objects

    def get_queryset(self):
        student_id = self.request.query_params.get('studentId')
        return self.queryset.filter(studentprofession_set__student_id=student_id)