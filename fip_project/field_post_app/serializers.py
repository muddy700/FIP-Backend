from .models import FieldPost, FieldApplication, FieldPostProfession
from rest_framework import serializers

class FieldPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = FieldPost
        fields = '__all__'

class FieldApplicationSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student_id.username", read_only=True)
    post_name = serializers.CharField(source="field_application_post_id.post_name", read_only=True)

    class Meta:
        model = FieldApplication
        fields = '__all__'
class FieldPostProfessionSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField(source="field_profession_post_id.post_name", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)

    class Meta:
        model = FieldPostProfession
        fields = '__all__'