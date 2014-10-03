from django.contrib import admin
from radio.models import Station

class StationAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_display_links = ('title', )
	search_fields = ('title', )	

admin.site.register(Station, StationAdmin)