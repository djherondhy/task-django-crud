from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa
from .serializers import TarefaSerializer

import json

@api_view(['GET'])
def get_tarefas(request):

    if request.method == 'GET':
        tarefas = Tarefa.objects.all()

        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH'])
def get_by_id(request, id):

    try:
        tarefa = Tarefa.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TarefaSerializer(tarefa, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        new_status = request.data.get('status')
        if new_status is None:
            return Response({'error': 'O novo status é necessário'}, status=status.HTTP_400_BAD_REQUEST)
        
        if new_status not in ['true', 'false']:
            return Response({'error': 'O novo status deve ser "true" ou "false"'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_status = new_status == 'true'
        tarefa.status = new_status
        tarefa.save()
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
   

@api_view(['GET', 'POST','PUT','DELETE'])
def tarefa_manager(request):
    
    #CREATE DATA (Post)
    if request.method == 'POST':

        new_task = request.data

        serializer = TarefaSerializer(data=new_task)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

    #UPDATE DATA (Put)
    if request.method == 'PUT':

        id_tarefa = request.data['id']
        updated_task = Tarefa.objects.get(pk=id_tarefa)

        print(request.data)

        serializer = TarefaSerializer(updated_task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    #DELETE DATA (Delete)

    if request.method == 'DELETE':
        try:
            task_to_delete = Tarefa.objects.get(pk=request.data['id'])
            task_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
  
        

    #GET F
    try:
        if request.GET['tarefa']:
            id_tarefa = request.GET['tarefa']
            
            try:
                tarefa = Tarefa.objects.get(pk=id_tarefa)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
        
    

