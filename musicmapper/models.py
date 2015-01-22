from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.TextField()
	mbid = models.CharField(max_length=36, blank=True) # This sould be the MBID xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
	skid = models.CharField(max_length=6, blank=True) # This should be the six-digit songkick ID of the artist
	def __unicode__(self):
		return self.name

class Song(models.Model):
	title = models.TextField()
	artist = models.ForeignKey(Artist)
	def __unicode__(self):
		return self.title

class Story(models.Model):
	storyId = models.IntegerField()
	title = models.TextField()
	description = models.TextField()
	date = models.DateTimeField()
	thumbnail = models.URLField()
	artists = models.ManyToManyField(Artist)
	songs = models.ManyToManyField(Song)
	def __unicode__(self):
		return self.title

class LocationSearchResult(models.Model):
	queryString = models.TextField()
	result = models.TextField()
	date = models.DateTimeField()