from django.conf.urls import patterns, url
from musicmapper import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^api/stories/$', views.story_list),
	url(r'^api/stories/(?P<pk>[0-9]+)/$', views.story_detail),
	url(r'^api/location-search/(?P<query>[\w ]+)/$', views.location_search),
)