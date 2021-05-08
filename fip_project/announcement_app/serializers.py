from .models import Announcement
from rest_framework import serializers

class AnnouncementSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source="source.designation_name", read_only=True)
    receiver = serializers.CharField(source="destination.designation_name", read_only=True)

    class Meta:
        model = Announcement
        fields = '__all__'
