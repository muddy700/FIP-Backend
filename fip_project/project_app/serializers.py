from .models import Project, ProjectMember
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    project_owner_name = serializers.CharField(source="project_owner.username", read_only=True)

    class Meta:
        model = Project
        fields = '__all__' 
class ProjectMemberSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source="member_id.username", read_only=True)
    project_name = serializers.CharField(source="project_id.project_name", read_only=True)

    class Meta:
        model = ProjectMember
        fields = '__all__' 