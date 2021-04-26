from rest_framework import generics, permissions
from .models import StudentProfile, StudentProfession, FieldReport
from .serializers import StudentProfileSerializer, StudentProfessionSerializer, FieldReportSerializer
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

class FieldReportViewSet(viewsets.ModelViewSet):
    queryset = FieldReport.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = FieldReportSerializer

class StudentProfessionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = StudentProfessionSerializer
    queryset = StudentProfession.objects

    def get_queryset(self):
        student_id = self.kwargs.get('studentId')
        return self.queryset.filter(student=student_id)