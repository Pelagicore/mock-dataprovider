from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact


class PaginatedContactSerializer(PaginationSerializer):
    class Meta:
        object_serializer_class = ContactSerializer




