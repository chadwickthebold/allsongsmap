import requests
import logging
import time
import os
import pytz
import xml.etree.ElementTree as ET
import datetime
from django.core.management.base import BaseCommand, CommandError
from musicmapper.models import Artist, Story, Song

logger = logging.getLogger(__name__)
dateFormat = '%a, %d %b %Y %H:%M:%S'

class Command(BaseCommand):
	args = '<>'
	help = 'Fully updates the database to the latest iteration of artists from the allsongs blog'
















































































	def processSong(self, songET, storyObj):
		"""

		"""

		# Create and save the song object in the Django model
		song = Song(title=songET.find('title').text)

		# Look for the artist name
		artistName = songET.find('artist').text
		if (artistName is None) or artistName == '':
			artistName = songET.find('album').find('albumArtist').text

		# Look for the artist. If the artist does not exist, create a new object
		if not Artist.objects.filter(name=artistName).exists():
			artistObj = Artist(name=artistName)
			artistObj.save()
			song.artist = artistObj
		else: 
			song.artist = Artist.objects.get(name=artistName)

		logger.info("Found Song : '%s' by '%s'" % (songET.find('title').text, artistName))
		song.save()

		# Save the song and the artist to the many-to-many fields of the containing story
		storyObj.songs.add(song)
		storyObj.artists.add(song.artist)
































































	def processStory(self, storyET):
		""" Process a given ASC Story

		"""

		# Create a date object for the story
		dateString = storyET.find('storyDate').text[:-5].strip()
		dateObj = datetime.datetime.strptime(dateString, dateFormat)
		dateObj = pytz.timezone("US/Eastern").localize(dateObj)


		logger.info("Found Story %s " % (storyET.attrib['id']))

		# Check if the story exists in the database. If it does not, create a new story and process all the songs
		if not Story.objects.filter(storyId=storyET.attrib['id']).exists():
			thumbnailURL = storyET.find('thumbnail')
			if not thumbnailURL is None:
				thumbnailURL = thumbnailURL.find('large')
				if not thumbnailURL is None:
					thumbnailURL = thumbnailURL.text
				else:
					thumbnailURL = ''
			else: 
				thumbnailURL = ''

			if not thumbnailURL.find('') == -1:
				thumbnailURL = thumbnailURL[:-5]

			story = Story(title=storyET.find('title').text, storyId=storyET.attrib['id'], description=storyET.find('teaser').text, thumbnail=thumbnailURL, date=dateObj)
			story.save()

			songList = storyET.findall('song')
			for song in songList:
				self.processSong(song, story)




































































	def callNPR(self):
		""" Perform a call to the NPR API to get ASC stories
		Continue to make calls until fewer than 50 stories are returned

		"""
		results = 50;
		payload = {
			"id" : "15709577",
			"apiKey" : self.nprKey,
			"fields" : "title,teaser,thumbnail,song,storyDate",
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
						dateString = element.find('storyDate').text[:-5].strip()
						dateObj = datetime.datetime.strptime(dateString, dateFormat)

						# Update the next request with the last date retrieved
						payload['endDate'] = str(dateObj.year)+'-'+str(dateObj.month)+'-'+str(dateObj.day)+' '+str(dateObj.hour)+':'+str(dateObj.minute)+':'+str(dateObj.second)

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







