from music.models import Track
from music.serializers import TrackSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('album', 'artist', 'title')
    search_fields = ('album', 'artist', 'title')


