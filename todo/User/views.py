import re
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from .models import User
from TodoBackend.models import Todo
from TodoBackend.serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# {
#     "user_name" : "Sumit",
#     "email" : "sumitpatel813@gmail.com",
#     "recovery_email" : "18bce236@nirmauni.ac.in",
#     "password" : "hariom15"
# }


@api_view(['POST', 'GET'])
def CreateUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # print(serializer.data['user_name'])
            return Response(serializer.data, status=201)
        else:
            return Response("Error Occured", status=400)

    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def DeleteUser(request):
    serializer = UserSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        try:
            # print(serializer.data)
            user = User.objects.get(
                user_name=serializer.data['user_name'], password=serializer.data['password'])
            # print(serializer.data['user_name'])
            user.delete()
            return Response("Successfully Deleted The User", status=201)
        except:
            return Response("User Does Not Exist", status=401)
    return Response("Serialization Error")


@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # print(serializer.data)
                user = User.objects.get(
                    user_name=serializer.data['user_name'], password=serializer.data['password'])
                # print(serializer.data['user_name'])
                user_serialized = UserSerializer(user)
                return Response(user_serialized.data, status=201)
            except:
                return Response("User Does Not Exist", status=401)
        else:
            return Response("Error Occured", status=400)


@api_view(['POST'])
def UserTask(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            # print(serializer.data)
            user = User.objects.get(
                user_name=serializer.data['user_name'], password=serializer.data['password'])
            # print(serializer.data['user_name'])
            user_serialized = UserSerializer(user)
            #print('\n\n',user_serialized.data['user_id'], '\n\n')
            try:
                tasks = Todo.objects.filter(
                    user_id=user_serialized.data['user_id'])
                task_serialized = TodoSerializer(tasks, many=True)
                return Response(task_serialized.data, status=201)
            except:
                return Response("Task Error")
        except:
            return Response("User Does Not Exist", status=401)
