from random import choice
from tracks.models import Track

frases = ['lol', 'hola', 'que','hace']

def basico(request):
	tracks =Track.objects.all()
	track = None
	for t in tracks:
		if request.path == t.get_absolute_url():
			track = t
			break
	return {'titulo': choice(frases),'tracks':tracks, 'selectedtrack': track}