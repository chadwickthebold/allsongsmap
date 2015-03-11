import os
import requests
import datetime
import pytz
import xml.etree.ElementTree as ET

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from musicmapper.models import Story, Artist, Song, LocationSearchResult, Location, Event
from musicmapper.serializers import StorySerializer, ArtistSerializer, LocationSearchResultSerializer, LocationSerializer, EventSerializer

# Helper class for json responses, from Django REST Framework
class JSONResponse(HttpResponse):
		"""
		An HttpResponse that renders its content into JSON.
		"""
		def __init__(self, data, **kwargs):
				content = JSONRenderer().render(data)
				kwargs['content_type'] = 'application/json'
				super(JSONResponse, self).__init__(content, **kwargs)














def index(request):
	"""
	Entry point for the application, should load the backbone frontend app
	"""
	return render(request, 'musicmapper/index.html', {})








































def location_search(request, query):
	"""
	Search the Songkick API for a location, returning a json collection of possible location matches
	These results will be cached for 30 days, as new locations probably don't show up too often
	"""
	skkey = os.environ['SONGKICKKEY']
	locationAPI = "http://api.songkick.com/api/3.0/search/locations.json" 

	# Check the database for an existing result before we attempt to hit the songkick api
	if not LocationSearchResult.objects.filter(queryString=query).exists():

		# Make a request to the Songkick location API
		response = requests.get(locationAPI, params={"apikey" : skkey,"query" : query})
		dateObj = pytz.timezone("US/Eastern").localize(datetime.datetime.now())

		# Cache the response
		locationResult = LocationSearchResult(queryString=query, result=response.text, date=dateObj)
		locationResult.save()

		# Directly return the Songkick result
		return HttpResponse(response.text, content_type="application/json")

	# Otherwise the result exists, and we return it from the db
	else : 
		return HttpResponse(LocationSearchResult.objects.get(queryString=query).result, content_type="application/json")





































def event_search_by_location(request, locationID):
	"""
	Retrieve the event calendar for a given metro area and cache it in the db
	"""




































def event_search(request, locationID, artistID):
	"""
	Search for an event with a given location ID and artist ID
	"""
























