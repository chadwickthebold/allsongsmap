from django.contrib import admin
from musicmapper.models import Artist
from musicmapper.models import Story
from musicmapper.models import Song

class ArtistAdmin(admin.ModelAdmin):
	fields = ['artistId', 'name']

class SongAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields': ['title']}),
		('Foreign Keys', {'fields': ['story', 'artist']})
	]

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Story)
admin.site.register(Song, SongAdmin)