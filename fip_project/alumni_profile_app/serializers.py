from .models import AlumniProfile, AlumniProfession
from rest_framework import serializers

class AlumniProfileSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="alumni.username", read_only=True)
    degree_program = serializers.CharField(source="program.program_name", read_only=True)
    department_name = serializers.CharField(source="department.department_name", read_only=True)
    organization_name = serializers.CharField(source="organization.username", read_only=True)

    class Meta:
        model = AlumniProfile
        fields = '__all__'

class AlumniProfessionSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="alumni.username", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = AlumniProfession
        fields = '__all__'