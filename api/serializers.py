from rest_framework import serializers
from app.models import *

#user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelsUser
        fields = ('id', 'username', 'password', 'bio', 'image', )

#project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModels
        fields = '__all__'

#task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModels
        fields = '__all__'
        