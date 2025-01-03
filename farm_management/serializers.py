from rest_framework import serializers
from .models import Crop, Land
from users.serializers import CustomUserSerializer

class CropSerializer(serializers.ModelSerializer):
    farmer_profile = CustomUserSerializer(source= 'farmer', read_only=True)
    
    class Meta:
        model = Crop
        fields = ['id', 'name', 'growth_stage','health_status','picture', 'farmer', 'farmer_profile']

class LandSerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True, read_only=True)

    class Meta:
        model = Land
        fields = ['id', 'size', 'location', 'farmer', 'crops']
