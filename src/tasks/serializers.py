from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class PaginatedTaskSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = TaskSerializer
