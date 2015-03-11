from musicmapper.models import Artist, Story, Song, Location, LocationSearchResult, Event
from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):
		class Meta:
			model = Story
			fields = ('id', 'storyId', 'title', 'description', 'date', 'thumbnail', 'artists', 'songs')

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = ('id','name','skid', 'mbid', 'sk_uri')

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ('title','artist')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('locationid','fullName', 'eventList')

class LocationSearchResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = LocationSearchResult
		fields = ('queryString','result', 'date')

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = ('eventid','locationRef', 'artists', 'title', 'uri')