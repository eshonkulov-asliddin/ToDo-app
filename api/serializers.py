from rest_framework import serializers
from tasks.models import Task
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    class Meta:
        model = Task
        fields = '__all__'

      