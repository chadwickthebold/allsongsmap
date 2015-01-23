from django.db import models

# Create your models here.

class Artist(models.Model):
	"""
	A featured artist
	"""
	name = models.TextField()
	mbid = models.CharField(max_length=36, blank=True) # This sould be the MBID xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
	skid = models.CharField(max_length=6, blank=True) # This should be the six-digit songkick ID of the artist
	sk_uri = models.TextField(blank=True)
	def __unicode__(self):
		return self.name

class Song(models.Model):
	"""
	The song performed by a featured artist
	"""
	title = models.TextField()
	artist = models.ForeignKey(Artist)
	def __unicode__(self):
		return self.title

class Story(models.Model):
	"""
	A story from the All Songs Considered Program
	"""
	storyId = models.IntegerField()
	title = models.TextField()
	description = models.TextField(blank=True)
	date = models.DateTimeField()
	thumbnail = models.URLField(blank=True)
	artists = models.ManyToManyField(Artist)
	songs = models.ManyToManyField(Song)
	def __unicode__(self):
		return self.title

class LocationSearchResult(models.Model):
	"""
	A JSON search result for a given location
	"""
	queryString = models.TextField()
	result = models.TextField()
	date = models.DateTimeField()
	def __unicode__(self):
		return self.queryString

class Event(models.Model):
	"""
	A Songkick Event
	"""
	eventid = models.CharField(max_length=10)
	locationRef = models.ForeignKey("Location")
	artists = models.ManyToManyField(Artist)
	title = models.TextField(blank=True)
	uri = models.TextField(blank=True)
	def __unicode__(self):
		return self.title

class Location(models.Model):
	"""
	A Songkick Metro Area
	"""
	locationid = models.CharField(max_length=10)
	fullName = models.TextField()
	eventList = models.ManyToManyField(Event)
	def __unicode__(self):
		return self.fullName