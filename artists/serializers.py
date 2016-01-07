from .models import Artist
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	filter_fields = ('id',)
	class Meta:
		model = Artist
		fields = ('id','first_name', 'last_name','biography', 'favorite_songs')