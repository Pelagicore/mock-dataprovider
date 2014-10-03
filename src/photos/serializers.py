from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo


class PaginatedPhotoSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = PhotoSerializer
