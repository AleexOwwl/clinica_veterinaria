from selenium import webdriver
import unittest

class NuevoPacienteTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_puedo_entrar_a_la_pagina_de_inicio(self):
		# Alex ha escuchado sobre una nueva clínica veterinaria en la
		# Universidad Autónoma de Zacatecas, la cual cuenta con una
		# página web donde puede solicitar una cita para su mascota.

		# El decide checar su página de inicio.
		self.browser.get('http://localhost:8000')

		# El nota que el título de la pagina menciona "Bienvenido a
		# Clínica Veterinaria UAZ".
		self.assertIn('Bienvenido', self.browser.title)
		self.fail('Prueba terminada!!!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')