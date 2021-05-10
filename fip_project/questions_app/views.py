from rest_framework import generics, permissions, viewsets
from .models import Question, MultipleChoice, ApplicantScore, ApplicantAnswer
from .serializers import (QuestionSerializer, 
MultipleChoiceSerializer, ApplicantScoreSerializer,
ApplicantAnswerSerializer)

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = QuestionSerializer

class MultipleChoicesViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoice.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MultipleChoiceSerializer

class ApplicantScoreViewSet(viewsets.ModelViewSet):
    queryset = ApplicantScore.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ApplicantScoreSerializer

class ApplicantAnswerViewSet(viewsets.ModelViewSet):
    queryset = ApplicantAnswer.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ApplicantAnswerSerializer
