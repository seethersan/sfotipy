from django.contrib import admin
from .models import Artist
from tracks.models import Track
from albums.models import Album

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class AlbumInLine(admin.StackedInline):
	model = Album
	extra = 1

class ArtistAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'biography')
	search_fields = ('first_name', 'last_name')
	# filter_horizontal = ('favorite_songs',)
	filter_vertical = ('favorite_songs',)
	inlines = [TrackInLine, AlbumInLine]
admin.site.register(Artist, ArtistAdmin)
