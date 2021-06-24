from .models import FieldPost, FieldApplication, FieldPostProfession, FieldPostProgram
from rest_framework import serializers

class FieldPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.username", read_only=True)

    class Meta:
        model = FieldPost
        fields = '__all__'

class FieldApplicationSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student.username", read_only=True)
    first_name = serializers.CharField(source="student.first_name", read_only=True)
    last_name = serializers.CharField(source="student.last_name", read_only=True)
    post_reference_number = serializers.CharField(source="post.reference_number", read_only=True)
    organization = serializers.IntegerField(source="post.organization_id", read_only=True)

    class Meta:
        model = FieldApplication
        fields = '__all__'
class FieldPostProfessionSerializer(serializers.ModelSerializer):
    post_reference_number = serializers.CharField(source="post.reference_number", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = FieldPostProfession
        fields = '__all__'

class FieldPostProgramSerializer(serializers.ModelSerializer):
    post_reference_number = serializers.CharField(source="post.reference_number", read_only=True)
    program_name = serializers.CharField(source="program.program_name", read_only=True)

    class Meta:
        model = FieldPostProgram
        fields = '__all__'