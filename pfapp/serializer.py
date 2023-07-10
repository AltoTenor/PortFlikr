from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    projects_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='project_name'
    )
    class Meta:
        model = Person
        fields = ['skills', 'occupation','user','projects_set']