from radio.models import Station
from radio.serializers import StationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter


class StationViewSet(ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title',)
    search_fields = ('title',)
