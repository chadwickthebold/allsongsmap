from django.conf.urls import patterns, url

from musicmapper import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')\
)