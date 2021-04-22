from .models import AlumniProfile, AlumniProfession
from rest_framework import serializers

class AlumniProfileSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="alumni_id.username", read_only=True)
    degree_program = serializers.CharField(source="program_id.program_name", read_only=True)
    department_name = serializers.CharField(source="department_id.department_name", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)

    class Meta:
        model = AlumniProfile
        fields = '__all__'

class AlumniProfessionSerializer(serializers.ModelSerializer):
    registration_number = serializers.CharField(source="alumni_id.username", read_only=True)
    profession_name = serializers.CharField(source="profession_id.profession_name", read_only=True)

    class Meta:
        model = AlumniProfession
        fields = '__all__'