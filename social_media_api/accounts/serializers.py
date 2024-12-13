from rest_framework import serializers
from .models import User 
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']
        
