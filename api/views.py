from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def task_create(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'Create a new task': True})


@api_view(['GET', 'DELETE'])
def task_delete(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data)


@api_view(['GET', 'PATCH'])
def task_update(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(
        task,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'all task': '/tasks',
        'add task': '/tasks/create/<id>',
        'update task': '/tasks/update/<id>',
        'delete task': '/tasks/destroy/<id>'
    }

    return Response(api_urls)
