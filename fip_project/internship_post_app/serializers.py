from .models import InternshipPost
from rest_framework import serializers

class InternshipPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = InternshipPost
        fields = '__all__'