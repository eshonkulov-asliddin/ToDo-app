import re
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from tasks.models import Task
from rest_framework.response import Response



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PATCH'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.user.profile.name == task.owner.name:
        task.description = 'Hello World. Cambridge'
        task.save()
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)    