from .models import FieldPost, FieldApplication, FieldPostProfession
from rest_framework import serializers

class FieldPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.username", read_only=True)

    class Meta:
        model = FieldPost
        fields = '__all__'

class FieldApplicationSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student.username", read_only=True)
    post_name = serializers.CharField(source="post.post_title", read_only=True)

    class Meta:
        model = FieldApplication
        fields = '__all__'
class FieldPostProfessionSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField(source="post.post_title", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = FieldPostProfession
        fields = '__all__'