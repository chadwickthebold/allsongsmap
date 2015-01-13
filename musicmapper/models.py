from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.TextField()
	artistId = models.CharField(max_length=32) # This sould be the MBID xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx,
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