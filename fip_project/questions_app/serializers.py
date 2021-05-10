from .models import Question, MultipleChoice, ApplicantScore, ApplicantAnswer
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)
    
    class Meta:
        model = Question
        fields = '__all__'

class MultipleChoiceSerializer(serializers.ModelSerializer):
    question_body = serializers.CharField(source="question.question_body", read_only=True)

    class Meta:
        model = MultipleChoice
        fields = '__all__'

class ApplicantScoreSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    post_description = serializers.CharField(source="post.post_description", read_only=True)

    class Meta:
        model = ApplicantScore
        fields = '__all__'

class ApplicantAnswerSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    post_description = serializers.CharField(source="post.post_description", read_only=True)
    question = serializers.CharField(source="question.question_body", read_only=True)
    selected_choice = serializers.CharField(source="choice.choice", read_only=True)

    class Meta:
        model = ApplicantAnswer
        fields = '__all__'
