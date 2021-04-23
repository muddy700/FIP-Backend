from .models import StudentProfile, StudentProfession
from rest_framework import serializers

class StudentProfileSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student_id.username", read_only=True)
    organization_name = serializers.CharField(source="organization_id.username", read_only=True)
    degree_program = serializers.CharField(source="program_id.program_name", read_only=True)
    department_name = serializers.CharField(source="department_id.department_name", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)
    academic_supervisor_name = serializers.CharField(source="academic_supervisor_id.username", read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'

class StudentProfessionSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student_id.username", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)

    class Meta:
        model = StudentProfession
        fields = '__all__'