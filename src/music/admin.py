from django.contrib import admin
from music.models import Track


class TrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'artist', 'title')
    list_display_links = ('album', 'artist', 'title')
    search_fields = ('album', 'artist', 'title')
    list_filter = ('album', 'artist', 'title')


admin.site.register(Track, TrackAdmin)