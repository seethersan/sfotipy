from django.test import TestCase
from .models import Artist

# Create your tests here.
class TestArtist(TestCase):
	def setUp(self):
		self.artist = Artist.objects.create(first_name='david', last_name='bowie')

	def test_existe_vista(self):
		res = self.client.get('/artist/%d/' % self.artist.id)
		self.assertEqual(res.status_code, 200)
		self.assertTrue('david' in res.content)

	def test_no_existe_vista(self):
		id_viejo = self.artist.id
		self.artist.delete()
		res = self.client.get('/artist/%d/' % id_viejo)
		self.assertEqual(res.status_code, 404)