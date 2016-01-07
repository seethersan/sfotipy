from __future__ import unicode_literals

from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField(blank=True)
	favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name="is_favorite_to")

	@staticmethod
	def autocomplete_search_fields():
		return ("id__exact", "first_name__icontains", "last_name__icontains")

	def __str__(self):
		return self.first_name + " " + self.last_name
