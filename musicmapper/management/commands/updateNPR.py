import requests
import logging
import time
import os
import xml.etree.ElementTree as ET
import datetime
from django.core.management.base import BaseCommand, CommandError
from musicmapper.models import Artist, Story, Song

logger = logging.getLogger(__name__)
dateFormat = '%a, %d %b %Y'

class Command(BaseCommand):
	args = '<>'
	help = 'Fully updates the database to the latest iteration of artists from the allsongs blog'























































	def processSong(self):
		"""

		"""



































































	def processStory(self, storyET):
		""" Process a given ASC Story

		"""

		dateString = storyET.find('storyDate').text[:-14].strip()
		dateObj = datetime.datetime.strptime(dateString, dateFormat)
		date = str(dateObj.year)+'-'+str(dateObj.month)+'-'+str(dateObj.day)

		logger.info("Found Story %s on %s : '%s'" % (storyET.attrib['id'], date, storyET.find('title').text))



		s = Story(title=storyET.find('title').text, storyId=storyET.attrib['id'], date=dateObj)

		s.save()


































































	def callNPR(self):
		""" Perform a call to the NPR API to get ASC stories
		Continue to make calls until fewer than 50 stories are returned

		"""
		results = 50;
		payload = {
			"id" : "15709577",
			"apiKey" : self.nprKey,
			"fields" : "title,song,storyDate",
			"output" : "NPRML",
			"endDate": "",
			"numResults" : "50"
		}
		
		nprAPI = "http://api.npr.org/query?"

		while results == 50:

			results = 0

			# Make the request to the NPR API
			response = requests.get(nprAPI, params=payload)

			# Fail out if we get 4XX or 5XX response
			if response.status_code != requests.codes.ok:
				logger.warning("Bad request -  got  %s" % (response.status_code))
				response.raise_for_status()

			# Create an ElementTree object from the response text
			nprml = ET.fromstring(response.text.encode('utf-8'))
			storyList = nprml.find("list")

			# Iterate through all returned stories
			for element in storyList:
				if element.tag == "story":
					results += 1 
					logger.info(results)

					# Get the new end date from the last response
					if results == 50:
						dateString = element.find('storyDate').text[:-14].strip()
						dateObj = datetime.datetime.strptime(dateString, dateFormat)
						payload['endDate'] = str(dateObj.year)+'-'+str(dateObj.month)+'-'+str(dateObj.day)

					# if the story contains a song, process it into the DB
					if not element.find('song') is None:
						self.processStory(element)


































































	def handle(self, *args, **options):
		self.nprKey = os.environ['NPRKEY']
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
		logger.info( 'Finished UpdateNPR command in %s:%s:%s' % (hours, minutes, seconds) )