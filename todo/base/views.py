from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Tasks
from .serializer import TasksSerializer
from django.contrib.auth.models import User



@api_view(['GET'])
def home(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def usertask(request,pk):
    user = User.objects.get(id=pk)
    task = user.tasks_set.all()
    serializer = TasksSerializer(task,many=True)
    return Response(serializer.data)
