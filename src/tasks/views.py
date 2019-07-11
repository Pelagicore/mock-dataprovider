from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'due', 'modified')
    search_fields = ('title', 'due', 'modified')
