from __future__ import unicode_literals

from django.db import models
from artists.models import Artist
from albums.models import Album

class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)			

	def __str__(self):
		return self.title + " - " + self.artist.first_name + " " + self.artist.last_name + " - " + self.album.title

	def get_absolute_url(self):
		return '/tracks/' + self.title + "/"

	def player(self):
		return """
		<audio controls>
			<source src="%s" type="audio/mpeg">
			Your browser does not support the audio tag
		</audio>
		""" % self.track_file.url
	player.allow_tags = True
	player.admin_order_field = 'track_file'

		
# Create your models here.
