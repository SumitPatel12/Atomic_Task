from django.db.models import fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['user_id','user_name', 'email', 'recovery_email', 'password', 'joining_date']

    # def validate_user_name(self, data):
    #     obj = User.objects.get(user_name = data['user_name'])
    #     if obj.exists() :
    #         raise serializers.ValidationError("Username Already Exists")