from django.conf.urls import patterns, url, include
from musicmapper import views

from musicmapper.models import Artist, Story, Song
from rest_framework import routers
from musicmapper.viewsets import StoryViewSet, ArtistViewSet, SongViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/location-search/(?P<query>[\w ]+)/$', views.location_search),
	url(r'^api/', include(router.urls)),
)