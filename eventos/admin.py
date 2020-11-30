from django.contrib import admin

# Register your models here.
from . models import reserva, servicio

admin.site.register(reserva)
admin.site.register(servicio)
