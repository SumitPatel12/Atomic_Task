import uuid
from .serializers import TodoSerializer
from .models import Todo
from User.serializers import UserSerializer
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def UserCreateTask(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else :
        return Response("Error!Failed to Create the Task!!", status=400)


@api_view(['POST'])
def UserUpdateTask(request):
    todo_id = uuid.UUID(request.data['todo_id'])
    # print(todo_id)
    try :
        task = Todo.objects.get(todo_id = todo_id)
        task.title = request.data['title']
        task.description = request.data['description']
        task.completed = request.data['completed']
        task.save()
        task_serialized = TodoSerializer(task)
        return Response(task_serialized.data, status =  200)
    except :
        return Response("Task Does Not Exist!!", status=400)


@api_view(['POST'])
def UserDeleteTask(request):
    todo_id = uuid.UUID(request.data['todo_id'])
    # print(todo_id)
    try :
        task = Todo.objects.get(todo_id = todo_id)
        task.delete()
        task_serialized = TodoSerializer(task)
        return Response("Successfully Deleted the Task", status =  200)
    except :
        return Response("Task Does Not Exist!!", status=400)


@api_view(['POST'])
def UserTask(request):
    user_id = uuid.UUID(request.data['user_id'])
    try:
        tasks = Todo.objects.filter(
            user_id=user_id)
        task_serialized = TodoSerializer(tasks, many=True)
        return Response(task_serialized.data, status=201)
    except:
        return Response("Task Error")