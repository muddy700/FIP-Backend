from .models import InternshipPost, InternshipApplication, InternshipPostProfession
from rest_framework import serializers

class InternshipPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = InternshipPost
        fields = '__all__'

class InternshipApplicationSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="alumni_id.username", read_only=True)
    post_name = serializers.CharField(source="internship_application_post_id.post_name", read_only=True)

    class Meta:
        model = InternshipApplication
        fields = '__all__'
class InternshipPostProfessionSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField(source="internship_profession_post_id.post_name", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)

    class Meta:
        model = InternshipPostProfession
        fields = '__all__'