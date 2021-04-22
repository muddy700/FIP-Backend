from .models import OrganizationAddress
from rest_framework import serializers

class OrganizationAddressSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = OrganizationAddress
        fields = '__all__' 