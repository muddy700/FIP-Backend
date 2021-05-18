from rest_framework import generics, permissions, viewsets
from .models import ( InternshipPost, InternshipApplication,
 InternshipApplicationStatus, ApplicantLevel, InterviewSchedule )
from .serializers import (InternshipPostSerializer, 
 InternshipApplicationSerializer, 
 InternshipApplicationStatusSerializer, 
 ApplicantLevelSerializer, InterviewScheduleSerializer )

class InternshipPostViewSet(viewsets.ModelViewSet):
    queryset = InternshipPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipPostSerializer

class InternshipApplicationViewSet(viewsets.ModelViewSet):
    queryset = InternshipApplication.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipApplicationSerializer

   
class InternshipApplicationStatusViewSet(viewsets.ModelViewSet):
    queryset = InternshipApplicationStatus.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InternshipApplicationStatusSerializer

   
class ApplicantLevelViewSet(viewsets.ModelViewSet):
    queryset = ApplicantLevel.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ApplicantLevelSerializer

class InterviewScheduleViewSet(viewsets.ModelViewSet):
    queryset = InterviewSchedule.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = InterviewScheduleSerializer

   