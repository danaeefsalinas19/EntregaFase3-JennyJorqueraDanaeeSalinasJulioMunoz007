from django.test import TestCase
from eventos.models import reserva

class reservaTestCase(TestCase):
    
    


    def setUp(self):
    
    
        testReserva1=reserva.objects.create(id = "1111")

        testReserva2=reserva.objects.create(id = "2222")

