from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie


class PaginatedMovieSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = MovieSerializer
