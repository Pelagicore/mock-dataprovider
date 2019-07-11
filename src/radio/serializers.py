from rest_framework import serializers
from radio.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        exclude = []