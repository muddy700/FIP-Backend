from .models import Certificate
from rest_framework import serializers

class CertificateSerializer(serializers.ModelSerializer):
    certificate_owner_name = serializers.CharField(source="certificate_owner.username", read_only=True)

    class Meta:
        model = Certificate
        fields = '__all__' 