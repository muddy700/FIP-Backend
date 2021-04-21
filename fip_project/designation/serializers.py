from .models import Designation
from rest_framework import serializers

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__' 