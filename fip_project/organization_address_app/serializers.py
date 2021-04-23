from .models import OrganizationProfile
from rest_framework import serializers

class OrganizationProfileSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.username", read_only=True)

    class Meta:
        model = OrganizationProfile
        fields = '__all__' 