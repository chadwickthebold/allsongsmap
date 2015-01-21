from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from musicmapper.models import Story, Artist, Song
from musicmapper.serializers import StorySerializer






def index(request):
	return HttpResponse("Hello, world! This is the musicmapper index.")



class JSONResponse(HttpResponse):
		"""
		An HttpResponse that renders its content into JSON.
		"""
		def __init__(self, data, **kwargs):
				content = JSONRenderer().render(data)
				kwargs['content_type'] = 'application/json'
				super(JSONResponse, self).__init__(content, **kwargs)



def story_list(request):
		"""
		List all stories
		"""
		if request.method == 'GET':
				stories = Story.objects.all()
				serializer = StorySerializer(stories, many=True)
				return JSONResponse(serializer.data)



def story_detail(request, pk):
		"""
		Retrieve a story with its details
		"""
		try:
				story = Story.objects.get(pk=pk)
		except Story.DoesNotExist:
				return HttpResponse(status=404)

		if request.method == 'GET':
				serializer = StorySerializer(story)
				return JSONResponse(serializer.data)







