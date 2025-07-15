from .models import RatingModel
from rest_framework import serializers

class RatingSerialzier(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = '__all__'