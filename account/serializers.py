from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            fullname = validated_data['fullname'],
            password = validated_data['password'],
            phone = validated_data['phone'],
            role = validated_data.get('role','user')
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['fullname'] = self.user.fullname
        data['role'] = self.user.role
        return data
