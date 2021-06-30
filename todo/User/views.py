from .serializers import UserSerializer
from .models import User
from TodoBackend.models import Todo
from TodoBackend.serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid

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
            return Response(status=201)
        else:
            return Response("Error Occured", status=400)

    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def DeleteUser(request):
    try:
        user_id = uuid.UUID(request.data['user_id'])
        user = User.objects.get(user_id=user_id)
        user.delete()
        return Response("Successfully Deleted The User", status=201)
    except:
        return Response("User Does Not Exist", status=401)


@api_view(['POST'])
def Login(request):
    try:
        user = User.objects.get(
            user_name=request.data['user_name'], password=request.data['password'])
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data['user_id'], status=201)
    except:
        return Response("User Does Not Exist", status=401)
