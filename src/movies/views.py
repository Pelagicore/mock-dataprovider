from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'year', 'genre')
    search_fields = ('title', 'year', 'genre')
