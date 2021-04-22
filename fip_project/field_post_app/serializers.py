from .models import FieldPost
from rest_framework import serializers

class FieldPostSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source="organization_id.organization_name", read_only=True)

    class Meta:
        model = FieldPost
        fields = '__all__'