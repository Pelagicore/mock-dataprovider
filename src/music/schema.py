import graphene

from graphene_django.types import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

class Query(object):
    all_tracks = graphene.List(TrackType)

    def resolve_all_tracks(self, info, **kwargs):
        return Track.objects.all()