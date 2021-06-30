from django.urls import path, include
from .views import CreateUser, DeleteUser, Login


urlpatterns = [
    path('create/', CreateUser),
    path('delete/', DeleteUser),
    path('login/', Login),
    # path('tasks/', UserTask),
]
