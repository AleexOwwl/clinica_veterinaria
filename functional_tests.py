from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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

		# Él nota que el título de la pagina menciona "Bienvenido a
		# Clínica Veterinaria UAZ".
		self.assertIn('Clínica Veterinaria', self.browser.title)
		header_text = self.browser.find_element_By_tag_name('h1').text
		self.assertIn('Bienvenido', header_text)

		# Él es invitado a registrar el nombre de su mascota.
		inputbox_pet = self.browser.find_element_by_id('id_name_pet')
		self.assertEqual(
			inputbox_pet.get_attribute('placeholder'),
			'Nombre de la mascota'
		)

		# Él escribe "Booster" en un cuadro de texto (La mascota
 		# de Alex es un dálmata).
 		inputbox_pet.send_keys('Booster')

 		# Además a Alex se le pide que ingrese su nombre o 
 		# nombre del propietario de la mascota.
		inputbox_owner = self.browser.find_element_by_id('id_name_owner')
		self.assertEqual(
			inputbox_pet.get_attribute('placeholder'),
			'Nombre del propietario'
		)

		# Él ingresa su nombre "Alex" en un cuadro de texto.
 		inputbox_owner.send_keys('Alex')

 		# Por último a Alex se le pide que ingrese la fecha 
 		# en la que desea su cita.
		inputbox_date = self.browser.find_element_by_id('id_appointment_date')
		self.assertEqual(
			inputbox_pet.get_attribute('placeholder'),
			'Fecha de la cita'
		)

		# A Alex le urge llevar a su mascota y solicita cita
		# para el 6 de junio.
 		inputbox_owner.send_keys('2018-06-06')

 		# Cuando Alex da clic en el boton guardar, la página 
 		# se actualiza y aparece la lista de citas pendientes.
 		# "1: Booster / Alex / 2018-06-06"
 		button_save = self.browser.find_element_by_id('id_button_save').click()
 		time.sleep(2)

 		table = self.browser.find_element_by_id('id_list_table')
 		rows = table.find_elements_by_tag_name('tr')
 		self.assertTrue(
 			any(row.text == '1: Booster / Alex / 2018-06-06' for row in rows),
 			"Nueva cita para mascota no apareció en la tabla"
 		)

		self.fail('Prueba terminada!!!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
