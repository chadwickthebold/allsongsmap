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
		