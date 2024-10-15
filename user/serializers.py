from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', "is_active", "date_joined" ,'is_staff', 'groups', 'user_permissions']
    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name must contain only letters.")
        return value
    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only letters.")
        return value
    def validate_number(self, value):
        if not value.startswith('5'):
            raise serializers.ValidationError("Phone number must start with 5.")
        
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only integers.")
        
        if len(value) != 9:
            raise serializers.ValidationError("Phone number must be 9 characters long.")
        return value
    
    
    
    class UserPasswordSerializer(serializers.Serializer):
        max_length=1000

    @staticmethod
    def validate_password(value):
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        validated_data['password'] = make_password(validated_data['password'])  
        return super().create(validated_data)
