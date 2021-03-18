from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from main.models import List, Task
from main.serializers import ListSerializer, TaskSerializer, CreateUpdateTaskSerializer


class ListApiView(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (AllowAny, )


class TaskViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )

    def list(self, request, list_id):
        tasks = Task.objects.get_incomplete_tasks(request, list_id)
        if tasks is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)

    def retrieve(self, request, list_id, task_id):
        tasks = Task.objects.get_task(request, list_id, task_id)
        if tasks is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = TaskSerializer(tasks)
            return Response(serializer.data)

    def create(self, request, list_id):
        data = {
            "task": request.data.get("task"),
            "due_on": request.data.get("due_on"),
            "owner_id": request.user.id,
            "mark": request.data.get("mark"),
            "list_id": list_id
        }
        serializer = CreateUpdateTaskSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, list_id, task_id=None):
        data = {
            "task": request.data.get("task"),
            "due_on": request.data.get("due_on"),
            "owner_id": request.user.id,
            "mark": request.data.get("mark"),
            "list_id": list_id
        }
        serializer = CreateUpdateTaskSerializer(instance=Task.objects.get_task(request, list_id, task_id),
                                                data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, list_id, task_id=None):
        try:
            task = Task.objects.get_task(request, list_id, task_id)
            task.delete()
            return Response(status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CompletedViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, list_id):
        tasks = Task.objects.get_completed_tasks(request, list_id)
        if tasks is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
