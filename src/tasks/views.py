from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'due', 'modified')
    search_fields = ('title', 'due', 'modified')
