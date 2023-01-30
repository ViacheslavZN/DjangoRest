from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, Users, TODO, Status
from .serializers import ProjectModelSerializer, UsersModelSerializer, StatusModelSerializer, ToDoModelSerializer


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer


class StatusModelViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = ToDoModelSerializer
