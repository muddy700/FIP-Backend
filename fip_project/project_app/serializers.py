from .models import Project, ProjectMember
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    # owner_name = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Project
        fields = '__all__' 
class ProjectMemberSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source="member.username", read_only=True)
    project_title = serializers.CharField(source="project.title", read_only=True)
    project_year = serializers.CharField(source="project.year", read_only=True)
    project_sponsor = serializers.CharField(source="project.sponsor", read_only=True)
    project_report = serializers.CharField(source="project.report", read_only=True)
    project_date_added = serializers.CharField(source="project.date_added", read_only=True)
    project_date_update = serializers.CharField(source="project.date_updated", read_only=True)
    project_recommendation_status = serializers.BooleanField(source="project.recommendation_status", read_only=True)
    # project_data = ProjectSerializer()

    class Meta:
        model = ProjectMember
        fields = '__all__' 