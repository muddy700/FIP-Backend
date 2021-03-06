from .models import (InternshipPost, InternshipApplication,
 InternshipApplicationStatus, ApplicantLevel, InterviewSchedule)
from rest_framework import serializers

class InternshipPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = InternshipPost
        fields = '__all__'

class InternshipApplicationSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    organization_name = serializers.CharField(source="post.organization.first_name", read_only=True)
    organization_id = serializers.CharField(source="post.organization.id", read_only=True)
    post_profession = serializers.CharField(source="post.profession.profession_name", read_only=True)
    profession_id = serializers.CharField(source="post.profession.id", read_only=True)
    post_status = serializers.CharField(source="post.status", read_only=True)
    post_reference = serializers.CharField(source="post.reference_number", read_only=True)
    post_capacity = serializers.CharField(source="post.post_capacity", read_only=True)
    post_description = serializers.CharField(source="post.post_description", read_only=True)
    reporting_instructions = serializers.CharField(source="post.reporting_instructions", read_only=True)

    class Meta:
        model = InternshipApplication
        fields = '__all__'
class InternshipApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipApplicationStatus
        fields = '__all__'

class ApplicantLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantLevel
        fields = '__all__'
class InterviewScheduleSerializer(serializers.ModelSerializer):
    post_description= serializers.CharField(source="post.post_description", read_only=True)
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)

    class Meta:
        model = InterviewSchedule
        fields = '__all__'