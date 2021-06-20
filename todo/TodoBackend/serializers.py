from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields = ['todo_id', 'title', 'description', 'completed', 'user_id']