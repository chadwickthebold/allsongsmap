from django.conf.urls import patterns, url
from musicmapper import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^stories/$', views.story_list),
	url(r'^stories/(?P<pk>[0-9]+)/$', views.story_detail),
)