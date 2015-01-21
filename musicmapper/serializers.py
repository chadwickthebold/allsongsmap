from musicmapper.models import Artist, Story, Song
from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Story
		fields = ('id', 'storyId', 'title', 'description', 'date', 'thumbnail', 'artists', 'songs')