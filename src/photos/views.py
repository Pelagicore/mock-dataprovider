from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'timestamp')
    search_fields = ('title', 'timestamp')
