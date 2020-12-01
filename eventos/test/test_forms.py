from django.test import TestCase
from  .forms import ReservaForm,ServicioForm
from .models import reserva, servicio
from django.core.files.uploadedfile import SimpleUploadedFile

class ReservaFormsTest(TestCase):
    def test_valid_form(self):
        r = reserva.objects.create(Nombre='Prueba1', Apellido='Prueba')
        data = {'nom_cliente': r.Nombre, 'apell_cliente': r.Apellido,}
        form = ReservaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        r = reserva.objects.create(nom_cliente='', Apellido='Prueba')
        data = {'nom_cliente': r.nom_cliente, 'apell_cliente': r.apell_cliente,}
        form = ReservaForm(data=data)
        self.assertFalse(form.is_valid())

