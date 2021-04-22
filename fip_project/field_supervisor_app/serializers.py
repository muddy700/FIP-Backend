from .models import FieldSupervisorProfile
from rest_framework import serializers

class FieldSupervisorProfileSerializer(serializers.ModelSerializer):
    supervisor_name = serializers.CharField(source="user_id.username", read_only=True)
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = FieldSupervisorProfile
        fields = '__all__' 