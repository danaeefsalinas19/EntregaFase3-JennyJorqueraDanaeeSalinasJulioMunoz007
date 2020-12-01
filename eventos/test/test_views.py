from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from eventos.models import reserva

class ReservaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_reserva = 5

        for reserva_id in range(number_of_reserva):
            reserva.objects.create(
                name=f'Accion {reserva_id}',
                summary=f'Prueba {reserva_id}',
            )
           
    
