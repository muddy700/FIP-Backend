from .models import InternshipPost, InternshipApplication
from rest_framework import serializers

class InternshipPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.username", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = InternshipPost
        fields = '__all__'

class InternshipApplicationSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    organization_name = serializers.CharField(source="post.organization.username", read_only=True)
    organization_id = serializers.CharField(source="post.organization.id", read_only=True)
    post_profession = serializers.CharField(source="post.profession.profession_name", read_only=True)
    post_capacity = serializers.CharField(source="post.post_capacity", read_only=True)
    post_description= serializers.CharField(source="post.post_description", read_only=True)

    class Meta:
        model = InternshipApplication
        fields = '__all__'