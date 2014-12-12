import requests
import logging
import time
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from musicmapper.models import Artist, Story, Song

logger = logging.getLogger(__name__)

class Command(BaseCommand):
	args = '<>'
	help = 'Fully updates the database to the latest iteration of artists from the allsongs blog'
	nprKey = os.environ['NPRKEY']









	def processSong(self):
		"""

		"""


















	def processStory(self):
		""" Process a given ASC Story

		"""






















	def callNPR(self):
		""" Perform a call to the NPR API to get ASC stories
		Continue to make calls until fewer than 20 stories are returned

		"""
		results = 0;






		if results == 20:
			callNPR()

















	def handle(self, *args, **options):
		logger.info('started NPR update command')

		# Get time for logging
		startTime = time.time()




		# Get ASC stories in chuncks of 20, until there are fewer than 20 results returned
		self.callNPR()


		# Get end time and write finish statement to logging
		endTime = time.time()
		runTimeS = startTime - endTime
		hours,remainder = divmod(runTimeS, 3600)
		minutes,seconds = divmod(remainder, 60)
		logger.info( '%s:%s:%s' % (hours, minutes, seconds) )