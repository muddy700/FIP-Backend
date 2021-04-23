from .models import FieldSupervisorProfile
from rest_framework import serializers

class FieldSupervisorProfileSerializer(serializers.ModelSerializer):
    supervisor_name = serializers.CharField(source="supervisor_id.username", read_only=True)
    organization_name = serializers.CharField(source="organization_id.username", read_only=True)
    designation_name = serializers.CharField(source="designation_id.designation_name", read_only=True)

    class Meta:
        model = FieldSupervisorProfile
        fields = '__all__' 