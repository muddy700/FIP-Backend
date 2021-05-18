from .models import OrganizationProfile, Contract
from rest_framework import serializers

class OrganizationProfileSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.username", read_only=True)

    class Meta:
        model = OrganizationProfile
        fields = '__all__' 

class ContractSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.username", read_only=True)
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = Contract
        fields = '__all__' 