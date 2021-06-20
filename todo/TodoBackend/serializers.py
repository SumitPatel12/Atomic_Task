from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title_id', 'title', 'description', 'status']
