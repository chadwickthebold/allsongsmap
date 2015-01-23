from django.conf.urls import patterns, url
from musicmapper import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/stories/$', views.story_list),
	url(r'^api/stories/pk/(?P<pk>[0-9]+)/$', views.story_detail),
	url(r'^api/artists/$', views.artist_list),
	url(r'^api/artists/pk/(?P<pk>[0-9]+)/$', views.artist_detail),
	url(r'^api/location-search/(?P<query>[\w ]+)/$', views.location_search),
)