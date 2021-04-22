from .models import StaffProfile
from rest_framework import serializers

class StaffProfileSerializer(serializers.ModelSerializer):
    staff_name = serializers.CharField(source="staff_id.username", read_only=True)
    department_name = serializers.CharField(source="department_id.department_name", read_only=True)

    class Meta:
        model = StaffProfile
        fields = '__all__'