from django import forms

from . models import reserva, servicio

class ReservaForm(forms.ModelForm):
    Nombre = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    Comentarios = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = reserva
        fields = ('Nombre', 'v',)

class ServicioForm(forms.ModelForm):
    nom_servicio = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    precio_por_persona = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
     descripcion = forms.TextField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
  

             
    class Meta:
        model = servicio
        fields = ('nom_servicio','precio_por_persona','descripcion')