from .models import StudentProfile, StudentProfession, FieldReport
from rest_framework import serializers

class StudentProfileSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student.username", read_only=True)
    first_name = serializers.CharField(source="student.first_name", read_only=True)
    last_name = serializers.CharField(source="student.last_name", read_only=True)
    email = serializers.CharField(source="student.email", read_only=True)
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)
    degree_program = serializers.CharField(source="program.program_name", read_only=True)
    degree_program_years = serializers.IntegerField(source="program.program_duration_years", read_only=True)
    department_name = serializers.CharField(source="department.department_name", read_only=True)
    # profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)
    academic_supervisor_name = serializers.CharField(source="academic_supervisor.username", read_only=True)
    academic_supervisor_email = serializers.CharField(source="academic_supervisor.email", read_only=True)
    # academic_supervisor_phone = serializers.CharField(source="academic_supervisor.phone", read_only=True)
    academic_supervisor_first_name = serializers.CharField(source="academic_supervisor.first_name", read_only=True)
    academic_supervisor_last_name = serializers.CharField(source="academic_supervisor.last_name", read_only=True)
    field_supervisor_name = serializers.CharField(source="field_supervisor.username", read_only=True)

    class Meta:
        model = StudentProfile
        fields = '__all__'

class StudentProfessionSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student.username", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = StudentProfession
        fields = '__all__'

class FieldReportSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="student.username", read_only=True)

    class Meta:
        model = FieldReport
        fields = '__all__'
