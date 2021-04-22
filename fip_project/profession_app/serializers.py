from .models import Profession
from rest_framework import serializers

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__' 