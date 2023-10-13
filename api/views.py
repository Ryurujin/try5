from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from .permissions import *

from app.models import *
from .serializers import *


#user
@api_view(['GET', 'POST'])
@permission_classes([UserPermission])
def User_views_list(request):
    
    users = ModelsUser.objects.all()

    if request.method == 'GET':
        serializers = UserSerializer(users, many=True, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = UserSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([UserDetailPermission])
def User_views_detail(request, pk):
    users = ModelsUser.objects.get(pk=pk)

    if request.method == 'GET':
        serializers = ModelsUser(users, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)

    elif request.method == 'PUT':
        #
        serializers = UserSerializer(data=request.data, context={'request': request})

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        users.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#project
@api_view(['GET', 'POST'])
@permission_classes([ProjectPermission])
def Project_views_list(request):
    if request.method == 'GET':
        projects = ProjectModels.objects.all()
        serializers = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        #
        serializers = ProjectSerializer(data=request.data, context={'request': request})
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProjectDetailPermission])
def Project_views_detail(request, pk):
    projects = projects.objects.get(pk=pk)

    if request.method == 'GET':
        serializers = ProjectSerializer(projects, context={'request': request})
        return Response(serializers.data, status=HTTP_200_OK)

    elif request.method == 'PUT':
        serializers = ProjectSerializer(projects, data=request.data, )#context={'request': request})

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        projects.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
#task 
@api_view(['GET', 'POST'])
@permission_classes([TaskPermission])
def Task_views_list(request, pk):
        tasks = TaskModels.objects.get(pk=pk)

        if request.method == 'GET':
            serializers = TaskSerializer(tasks, many=True)
            return Response(serializers.data, status=HTTP_200_OK)

        elif request.method == 'POST':
            serializers = TaskSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TaskDetailPermission])
def Task_views_detail(request, pk):
    tasks = TaskModels.objects.get(pk=pk)

    if request.method == 'GET':
        serializers = TaskSerializer(tasks)
        return Response(serializers.data, status=HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializers = TaskSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tasks.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    