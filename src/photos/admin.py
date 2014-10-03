from django.contrib import admin
from photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    list_display_links = ('title', 'timestamp')
    search_fields = ('title', 'timestamp')
    list_filter = ('title', 'timestamp')

admin.site.register(Photo, PhotoAdmin)
