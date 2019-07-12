from django.urls import path, include, re_path
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from graphene_django.views import GraphQLView

import contacts

from movies.views import MovieViewSet
from music.views import TrackViewSet
from photos.views import PhotoViewSet
from radio.views import StationViewSet
from tasks.views import TaskViewSet
from contacts.views import ContactViewSet
from rest_framework import routers
from django.views.static import serve


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'music', TrackViewSet)
router.register(r'radio', StationViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'tasks', TaskViewSet)



urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'browse/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT, 
        'show_indexes': True
    }),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]


urlpatterns += staticfiles_urlpatterns()
#urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
