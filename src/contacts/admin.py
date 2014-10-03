from django.contrib import admin
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('given_name', 'surname', 'street_address', 'zip_code', 'city', 'country')
    list_display_links = ('given_name', 'surname')
    search_fields = ('given_name', 'surname', 'street_address', 'zip_code', 'city', 'country')


admin.site.register(Contact, ContactAdmin)