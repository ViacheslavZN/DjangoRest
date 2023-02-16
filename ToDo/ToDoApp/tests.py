import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectViewSet, ToDoModelViewSet, UsersModelViewSet
from .models import TODO, Project, Users
class TestProjectViewSet(TestCase):
    def test_get_list(self):
    factory = APIRequestFactory()
    request = factory.get('/api/projects/')
    view = ProjectViewSet.as_view({'get': 'list'})
    response = view(request)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


def test_get_detail(self):
    author = Users.objects.create(first_name='Иван', second_name='Петров')
    client = APIClient()
    response = client.get(f'/api/users/{user.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_get_detail_project(self):
    project = mixer.blend(Project, first__name='Иван')
    response = self.client.get(f'/api/projects/{project.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    response_project = json.loads(response.content)
    self.assertEqual(response_project['first']['name'], 'Иван')



