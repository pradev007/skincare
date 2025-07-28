from rest_framework import serializers
from . models import ExpertModel

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertModel
        fields = "__all__"