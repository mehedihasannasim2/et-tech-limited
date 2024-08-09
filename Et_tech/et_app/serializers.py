from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

from rest_framework import serializers
from .models import *
from .import views

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']




'''model serializer'''

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__' 


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__' 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' 


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__' 


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__' 


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__' 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 




