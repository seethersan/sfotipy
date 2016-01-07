from __future__ import unicode_literals

from django.db import models
from artists.models import Artist

class Album(models.Model):
	title = models.CharField(max_length=255)
	cover = models.FileField(upload_to='albums')
	artist = models.ForeignKey(Artist)

	def __str__(self):
		return self.title + " - " + self.artist.first_name + " " + self.artist.last_name