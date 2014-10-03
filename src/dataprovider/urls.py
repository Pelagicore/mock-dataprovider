from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import contacts

from movies.views import MovieViewSet
from music.views import TrackViewSet
from photos.views import PhotoViewSet
from radio.views import StationViewSet
from tasks.views import TaskViewSet
from contacts.views import ContactViewSet
from rest_framework import routers

admin.autodiscover()




urlpatterns = patterns('',
                       url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^browse/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
                       )

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'music', TrackViewSet)
router.register(r'radio', StationViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'tasks', TaskViewSet)
urlpatterns += router.urls


urlpatterns += staticfiles_urlpatterns()
#urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
