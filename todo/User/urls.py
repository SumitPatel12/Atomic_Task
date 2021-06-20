from django.urls import path, include
from .views import CreateUser, DeleteUser, Login, UserTask


urlpatterns = [
    path('create/', CreateUser),
    path('delete/', DeleteUser),
    path('login/', Login),
    path('tasks/', UserTask),
]
