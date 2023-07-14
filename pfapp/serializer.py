from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields=['role','company','desc']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project_name', 'url', 'desc']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']

class Personserializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    img = serializers.ImageField(required=False)
    img1 = serializers.ImageField(required=False)
    projects_set =  ProjectSerializer(many=True, read_only=True)
    work_set=WorkSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = ['user','img','img1','linkedin','github','occupation','skills','hobbies',"projects_set","work_set"]