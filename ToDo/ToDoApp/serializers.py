from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, Users, TODO, Status


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UsersModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class StatusModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
