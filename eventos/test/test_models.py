from django.test import TestCase
from eventos.models import reserva

class reservaTestCase(TestCase):
    
    
    @classmethod


    def setUp(self):
    
    
        testReserva1=reserva.objects.create(codigo_reserva = "1111")

        testReserva2=reserva.objects.create(codigo_reserva = "2222")

        reserva.objects.create(codigo_reserva = testReserva1, fecha_evento = "2020-11-28" ,nom_cliente = "Fernanda",apell_cliente = "Salinas",
            celu_cliente ="999999999",email = "jejejejj@gmail.com",cant_personas = "150",total = "100000")

        reserva.objects.create(codigo_reserva = testReserva2,fecha_evento = "2020-11-27" ,nom_cliente = "Danaee",apell_cliente = "Salinas",
            celu_cliente ="987177174",email = "jajaj@gmail.com",cant_personas = "150",total = "100000")

    def test_reserva(self):
        
        reserva1 = reserva.objects.get(fecha_evento = "2020-11-19" ,nom_cliente = "Fernanda",apell_cliente = "Salinas",
            celu_cliente ="999999999",email = "jejejejj@gmail.com",cant_personas = "150",total = "100000")
        self.assertEqual(reserva1.reserva.codigo_reserva, "1111")  

        reserva2 = reserva.objects.get(fecha_evento = "2020-11-27" ,nom_cliente = "Danaee",apell_cliente = "Salinas",
            celu_cliente ="987177174",email = "jajaj@gmail.com",cant_personas = "150",total = "100000")
        self.assertEqual(reserva2.reserva.codigo_reserva, "2222")


