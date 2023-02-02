from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Project, Users, TODO, Status
from .serializers import ProjectModelSerializer, UsersModelSerializer, StatusModelSerializer, ToDoModelSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class ToDoPagination(PageNumberPagination):
    page_size = 20

# Project
class ProjectViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        from django.db.models import Project_name
        project_name = Project_name
        return Project.objects.filter(name_contains=project_name)


# User
class UsersModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        users = Users.objects.all()
        serializer = UsersModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(Users, pk=pk)
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)

  def update(self, request, pk=None):
        user = update(Users, pk=pk)
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)


# ToDo
class ToDoModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = ToDoModelSerializer



class StatusModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Status.objects.all()
    serializer_class = StatusModelSerializer
    pagination_class = ToDoPagination

   def get_queryset(self):
        from django.db.models import Project_name
        project_name = Project_name
        return Project.objects.filter(name_contains=project_name)