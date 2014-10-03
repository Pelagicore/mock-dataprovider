from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from music.models import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track


class PaginatedTrackSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = TrackSerializer

