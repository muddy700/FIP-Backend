from .models import OrganizationProfile, Contract, Rating, Invitations, Notification, NotificationView
from rest_framework import serializers

class OrganizationProfileSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.first_name", read_only=True)
    organization_full_name = serializers.CharField(source="organization_id.last_name", read_only=True)
    organization_email = serializers.CharField(source="organization_id.email", read_only=True)
    pwd = serializers.CharField(source="organization_id.password", read_only=True)

    class Meta:
        model = OrganizationProfile
        fields = '__all__' 

class ContractSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    profession_name = serializers.CharField(source="profession.profession_name", read_only=True)

    class Meta:
        model = Contract
        fields = '__all__' 

class RatingSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)

    class Meta:
        model = Rating
        fields = '__all__' 

class InvitationsSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization.first_name", read_only=True)
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)

    class Meta:
        model = Invitations
        fields = '__all__' 

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__' 

class NotificationViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationView
        fields = '__all__' 