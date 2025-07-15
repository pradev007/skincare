from rest_framework import serializers
from .models import ProgramModel

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramModel
        fields = '__all__'