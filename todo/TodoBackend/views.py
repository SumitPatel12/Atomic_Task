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
    else:
        return Response("Error!Failed to Create the Task!!", status=400)


@api_view(['PUT'])
def UserUpdateTask(request, todo_id):
    cur_todo_id = uuid.UUID(todo_id)
    # print(todo_id)
    try:
        task = Todo.objects.get(todo_id=cur_todo_id)
        updated_task = TodoSerializer(task, data=request.data)
        if updated_task.is_valid():
            updated_task.save()
            return Response(updated_task.data, status=200)
        else:
            return Response("Could Not Update", status=400)
    except:
        return Response("Task Does Not Exist!!", status=400)


@api_view(['DELETE'])
def UserDeleteTask(request, todo_id):
    todo_id = uuid.UUID(todo_id)
    # print(todo_id)
    try:
        task = Todo.objects.get(todo_id=todo_id)
        task.delete()
        return Response("Successfully Deleted the Task", status=200)
    except:
        return Response("Task Does Not Exist!!", status=400)


@api_view(['GET'])
def UserTask(request, user_id):
    # print(args)
    # print(kwargs)
    curr_user_id = uuid.UUID(user_id)
    # return Response("XYZ")
    try:
        tasks = Todo.objects.filter(
            user_id=curr_user_id)
        task_serialized = TodoSerializer(tasks, many=True)
        return Response(task_serialized.data, status=201)
    except:
        return Response("Task Error")
