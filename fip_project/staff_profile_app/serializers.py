from .models import StaffProfile
from rest_framework import serializers

class StaffProfileSerializer(serializers.ModelSerializer):
    staff_name = serializers.CharField(source="staff.username", read_only=True)
    staff_first_name = serializers.CharField(source="staff.first_name", read_only=True)
    staff_last_name = serializers.CharField(source="staff.last_name", read_only=True)
    department_name = serializers.CharField(source="department.department_name", read_only=True)

    class Meta:
        model = StaffProfile
        fields = '__all__'