from django import forms
from .models import citas

class FormPet(forms.ModelForm):
	class Meta:
		model = pet_info
		fields = (
			'nombre_mascota',
			'nombre_propietario',
			'fecha_cita'
			)