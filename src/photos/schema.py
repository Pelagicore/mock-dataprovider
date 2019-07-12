import graphene

from graphene_django.types import DjangoObjectType

from .models import Photo

class PhotoType(DjangoObjectType):
    class Meta:
        model = Photo

class Query(object):
    all_photos = graphene.List(PhotoType)

    def resolve_all_photos(self, info, **kwargs):
        return Photo.objects.all()