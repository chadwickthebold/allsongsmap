from django.conf.urls import patterns, url

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from musicmapper.models import Story
from musicmapper.serializers import StorySerializer

from musicmapper import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')\
)

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)