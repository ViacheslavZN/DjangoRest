from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ToDoApp.views import ProjectModelViewSet
from ToDoApp.views import UsersModelViewSet
from ToDoApp.views import StatusModelViewSet
from ToDoApp.views import ToDoModelViewSet

router = DefaultRouter()
router.register('Projest', ProjectModelViewSet)
router.register('User', UsersModelViewSet)
router.register('Status', StatusModelViewSet)
router.register('ToDo', ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
