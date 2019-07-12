import graphene

from graphene_django.types import DjangoObjectType

from .models import Movie

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class Query(object):
    all_movies = graphene.List(MovieType)

    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()