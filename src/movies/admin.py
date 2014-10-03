from django.contrib import admin
from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre')
    list_display_links = ('title', 'year', 'genre')
    search_fields = ('title', 'year', 'genre')
    list_filter = ('title', 'year', 'genre')

admin.site.register(Movie, MovieAdmin)