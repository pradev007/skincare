# account/serializers.py
import re
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True, min_length = 8)
    phone = serializers.CharField(max_length = 10)
    class Meta:
        model = CustomUser
        fields = ['fullname', 'phone', 'password','role']
        extra_kwargs = {
            'role': {'default': 'user'},
            'is_active': {'read_only':True},
            'is_staff': {'read_only':True},
            'is_superuser': {'read_only':True}
        }

    def validate_phone (self,value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("phone number must be exactly 10 digits")
        return value
    

    
    def validate_role(self, value):
        """
        Prevent superadmin role creation via API.
        """
        if value == 'superadmin':
            raise serializers.ValidationError("Cannot create superadmin via API")
        return value
    
    def validate_password(self,value):
        has_uppercase = re.search(r'[A-Z]',value)
        has_digit = re.search(r'[0-9]',value)
        has_special = re.search(r'[!@#$%^&*]',value)

        if not all([has_uppercase,has_digit,has_special]):
            raise serializers.ValidationError('Password must contain atleast one uppercase,digit and special character')
        return value
    

    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            fullname = validated_data['fullname'],
            password = validated_data['password'],
            phone = validated_data['phone'],
            role = validated_data.get('role','user')
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICE)
    def validate(self, attrs):
        data = super().validate(attrs)
        # remove the below line to remove role-base login
        # if self.user.role != attrs['role']:
        #     raise serializers.ValidationError({'role':'invalid role for this user'})
        if not self.user.is_active:
            raise serializers.ValidationError({'non_field_errors':'Account is inactive'})
        
        # check if request came from API clients(eg,postman) and restrict them
        # request = self.context.get('request')
        # user_agent = request.META.get('HTTP_USER_AGENT', '')
        # if self.user.role == 'superadmin' and 'Postman' in user_agent:
        #     raise serializers.ValidationError({"non_field_errors": "Superadmin login is restricted to browser-based interfaces"})

        data['fullname'] = self.user.fullname
        data['phone'] = self.user.phone
        data['role'] = self.user.role
        return data
