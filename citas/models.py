# -*- coding: utf-8 -*-

from django.db import models

class pet_info(models.Model):
	nombre_mascota = models.CharField('Nombre de la mascota', max_length=100)
	nombre_propietario = models.CharField('Nombre del propietario', max_length=100)
	fecha_cita = models.DateField('Fecha de la cita', auto_now_add=True)

	def __str__(self):
		return self.nombre_mascota
