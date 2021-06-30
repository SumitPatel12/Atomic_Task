from django.urls import path
from .views import UserTask, UserCreateTask, UserUpdateTask, UserDeleteTask


urlpatterns = [
    path('user-task/<str:user_id>', UserTask),
    path('create-task/', UserCreateTask),
    path('update-task/<str:todo_id>', UserUpdateTask),
    path('delete-task/<str:todo_id>', UserDeleteTask),
]
