from random import choice
from django.shortcuts import redirect
paises = ['Mexico', 'Colombia', 'Peru']

def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):
		pais = de_donde_vengo(request)
		if pais == 'Mexico':
			return redirect('http://platzi.com')