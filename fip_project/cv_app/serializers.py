from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PersonalInformation, EducationInformation, ExperienceInformation
    
class PersonalInformationSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    alumni_phone_number = serializers.CharField(source="profile.phone", read_only=True)
    # alumni_image = serializers.CharField(source="profile.profile_image", read_only=True)
    email = serializers.CharField(source="alumni.email", read_only=True)
    first_name = serializers.CharField(source="alumni.first_name", read_only=True)
    last_name = serializers.CharField(source="alumni.last_name", read_only=True)

    class Meta:
        model = PersonalInformation
        fields = '__all__'

class EducationInformationSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    class Meta:
        model = EducationInformation
        fields = '__all__'

class ExperienceInformationSerializer(serializers.ModelSerializer):
    alumni_name = serializers.CharField(source="alumni.username", read_only=True)
    class Meta:
        model = ExperienceInformation
        fields = '__all__'
