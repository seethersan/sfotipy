from django.contrib import admin
from .models import Album
from sorl.thumbnail import get_thumbnail

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title','image_album')

	def image_album(self,obj):
		return '<img src="%s"/>' % get_thumbnail(obj.cover,'50x50').url
	image_album.allow_tags = True
admin.site.register(Album,AlbumAdmin)
# Register your models here.
