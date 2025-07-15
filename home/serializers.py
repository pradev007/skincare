from rest_framework import serializers
from .models import HeadingModel

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingModel
        fields = ['id', 'title', 'subtitle']