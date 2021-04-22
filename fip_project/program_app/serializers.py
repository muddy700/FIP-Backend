from .models import Program
from rest_framework import serializers

class ProgramSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = Program
        fields = '__all__' 