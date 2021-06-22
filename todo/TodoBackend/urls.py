from django.urls import path
from .views import UserTask, UserCreateTask, UserUpdateTask, UserDeleteTask


urlpatterns = [
    path('user-task/', UserTask),
    path('create-task/', UserCreateTask),
    path('update-task/', UserUpdateTask),
    path('delete-task/', UserDeleteTask),
]
