from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

	

class reserva(models.Model):
	"""Model representing an reserva."""
	id = models.CharField( primary_key=True, max_length=10)
	fecha_del_evento = models.DateField(null=True, blank=True)
	Servicio = models.ForeignKey('servicio', on_delete=models.SET_NULL, null=True, blank=False)
	Nombre = models.CharField(max_length=200)
	Apellido = models.CharField(max_length=200)
	Celular = models.CharField(max_length=10)
	Email = models.CharField(max_length=200)
	Cantidad_de_personas = models.IntegerField(default=0)
	Comentarios = models.TextField( null=True ,max_length=1000)


	def __str__(self):
		return self.id
	
	def get_absolute_url(self):
		return reverse('reserva_detalle', args=[str(self.id)])

class servicio(models.Model):
	"""Model representing an servicio."""

	id = models.CharField(primary_key=True, max_length=10)
	nom_servicio = models.CharField(max_length=200)
	precio_por_persona = models.CharField(max_length=10)

	descripcion = models.TextField(max_length=1000)

	def __str__(self):
		return self.nom_servicio

		
	def get_absolute_url(self):
		return reverse('servicio_detalle', args=[str(self.id)])

