import requests
import logging
import time
import os
import xml.etree.ElementTree as ET
import datetime
from django.core.management.base import BaseCommand, CommandError
from musicmapper.models import Artist, Story, Song

logger = logging.getLogger(__name__)
dateFormat = '%a, %d %b %Y %H:%M:%S'

class Command(BaseCommand):
	args = '<>'
	help = 'Get the Musicbrainz ID for a given artist, as well as the Songkick ID'

	def handle(self, *args, **options):
		skkey = os.environ['SONGKICKKEY']
		artistAPI = "http://api.songkick.com/api/3.0/search/artists.xml" 

		# Iterate through all artists in the db
		for artist in Artist.objects.all():
			if not artist.skid or not artist.mbid:
				query = artist.name
				response = requests.get(artistAPI, params={"apikey" : skkey, "query" : query})
				time.sleep(0.1)

				# Fail out if we get a bad response code
				if response.status_code != requests.codes.ok:
					response.raise_for_status()

				# Parse the result into an ElementTree
				result = ET.fromstring(response.text.encode('utf-8'))

				# Nothing to do if no results returned
				if not result.get("totalEntries") == "0":
					artistElem = result.find("results").find("artist")
					skid = artistElem.get("id")
					uri = artistElem.get("uri")
					artist.skid = skid
					artist.sk_uri = uri

					if artistElem.find("identifier") is not None:
						mbid = artistElem.find("identifier").get("mbid")
						artist.mbid = mbid
					
					artist.save()


