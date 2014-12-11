import requests
import logging
import xml.etree.ElementTree as ET
import musicbrainzngs
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from musicmapper.models import Artist, Story, Song

logger = logging.getLogger(__name__)

class Command(BaseCommand):
	args = '<>'
	help = 'Fully updates the database to the latest iteration of artists from the allsongs blog'

	def handle(self, *args, **options):
		print('attempting log')
		logger.info('started NPR update command')
		# Set the useragent for musicbrainz api requests
		#musicbrainzngs.set_useragent("allsongsmap", "0.01", "http://tylerchadwick.com")
		# Search for an artist
		#result = musicbrainzngs.search_artists(artist="Brody Dalle")
		