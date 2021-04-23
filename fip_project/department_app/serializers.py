from .models import Department
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    hod_name = serializers.CharField(source="department_hod.username", read_only=True)

    class Meta:
        model = Department
        fields = '__all__' 