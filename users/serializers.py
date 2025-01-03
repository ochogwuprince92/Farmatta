from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_farmer', 'is_buyer', 'address', 'phone_number']

class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'is_farmer', 'is_buyer', 'address', 'phone_number']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_farmer=validated_data.get('is_farmer', False),
            is_buyer=validated_data.get('is_buyer', False),
            address=validated_data.get('address', False),
            phone_number=validated_data.get('phone_number', False)
        )
        return user