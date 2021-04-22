from .models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    project_owner_name = serializers.CharField(source="project_owner.username", read_only=True)

    class Meta:
        model = Project
        fields = '__all__' 