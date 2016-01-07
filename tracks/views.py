from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
import json
from rest_framework import viewsets
from .serializers import TrackSerializer
from .task import demorada

class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
# Create your views here.
def track_view(request, title):
	# try:
	# 	track = Track.objects.get(title=title)
	# except Track.DoesNotExist:
	# 	raise Http404
	track = get_object_or_404(Track, title=title)
	# demorada.apply_async(countdown=5)
	data = {
		'title':track.title,
		'order':track.order,
		# 'track':track.track_file,
		'album':track.album.title,
		'artist':{
			'name':track.artist.first_name,
			'last_name':track.artist.last_name,
			'biography':track.artist.biography,
		}
	}
	# json_data = json.dumps(data)
	# return HttpResponse(json_data, content_type='application/json')
	return render(request, 'track.html', {'track':track})

