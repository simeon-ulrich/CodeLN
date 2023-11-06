from rest_framework import serializers
from .models import CustomUser, Model3d, Badge

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # Include specific fields as needed

class Model3dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3d
        fields = '__all__'  # Include specific fields as needed

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'  # Include specific fields as needed
