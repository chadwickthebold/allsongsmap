from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=200)
	artistId = models.CharField(max_length=32x) # This sould be the MBID xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx,
	def __unicode__(self):
		return self.name

class Story(models.Model):
	storyId = models.IntegerField()
	date = models.DateTimeField()
	def __unicode__(self):
		return self.storyId

class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.ForeignKey(Artist)
	story = models.ForeignKey(Story)
	def __unicode__(self):
		return self.title
