from django.contrib import admin
from django.urls import path, include
from TodoBackend import views as views_TodoBackend
from rest_framework import routers
from User import urls as user_urls

router = routers.DefaultRouter()
router.register(r'tasks', views_TodoBackend.TodoView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('user/', include(user_urls))
]
