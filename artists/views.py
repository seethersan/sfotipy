from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Artist
from rest_framework import viewsets
from .serializers import ArtistSerializer

# Create your views here.
class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'fav_artist'
	template_name = 'artist.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artist'
	template_name = 'artist.html'

class ArtistViewSet(viewsets.ModelViewSet):
	filter_fields = ('id',)
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
