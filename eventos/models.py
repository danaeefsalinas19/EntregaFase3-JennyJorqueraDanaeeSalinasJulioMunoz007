from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

	

class reserva(models.Model):
	"""Model representing an reserva."""
	id = models.CharField( primary_key=True, max_length=10)
	fecha_evento = models.DateField(null=True, blank=True)
	nom_cliente = models.CharField(max_length=200)
	apell_cliente = models.CharField(max_length=200)
	celu_cliente = models.CharField(max_length=10)
	email = models.CharField(max_length=200)
	cant_personas = models.IntegerField(default=0)
	total = models.IntegerField(default=0)

	def __str__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('reserva_detalle', args=[str(self.id)])

class servicio(models.Model):
	"""Model representing an servicio."""

	id = models.CharField(primary_key=True, max_length=10)
	nom_servicio = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	precio_por_persona = models.CharField(max_length=10)
	image= models.ImageField(upload_to='images/', null=True, blank=True)

	def __str__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('servicio_detalle', args=[str(self.id)])

