from .models import Services
from rest_framework import serializers

class ServicesSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"