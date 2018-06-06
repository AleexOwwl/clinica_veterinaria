from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from citas.views import home_page

class HomePageTest(TestCase):

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'pet_text': 'Nueva mascota en lista'})
		self.assertIn('Nueva mascota en lista', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')
