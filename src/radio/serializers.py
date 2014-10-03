from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from radio.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station


class PaginatedStationSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = StationSerializer
