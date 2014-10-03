from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('given_name', 'surname', 'street_address', 'zip_code', 'city', 'country')
    search_fields = ('given_name', 'surname', 'street_address', 'zip_code', 'city', 'country')

