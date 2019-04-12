from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, read_only=True)  # disable username editing

    class Meta:
        model = User
        fields = ['username', 'group', 'email', 'status']
