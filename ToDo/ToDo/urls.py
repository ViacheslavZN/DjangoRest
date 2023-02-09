from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ToDo.ToDoApp.views import ProjectViewSet
from ToDo.ToDoApp.views import UsersModelViewSet
from ToDo.ToDoApp.views import StatusModelViewSet
from ToDo.ToDoApp.views import ToDoModelViewSet

router = DefaultRouter()
router.register('Projest', ProjectViewSet)
router.register('User', UsersModelViewSet)
router.register('Status', StatusModelViewSet)
router.register('ToDo', ToDoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
