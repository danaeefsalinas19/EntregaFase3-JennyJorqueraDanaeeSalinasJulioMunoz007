from django.shortcuts import render
from . models import reserva, servicio
from django.views import generic

#importamos información para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    num_reserva = reserva.objects.all().count()
   
    return render(
        request,
        'index.html',
        context={'num_reserva': num_reserva},
    )

def eventos(request):
   
    return render(
        request,
        'eventos.html',
    )

def cotizacion(request):
   
    return render(
        request,
        'cotizacion.html',
      
    )

def descEventos(request):
   
    return render(
        request,
        'descEventos.html',
      
    )

def reservas(request):
    
    return render(
        request,
        'reservas.html',
    )





class reservaCreate(CreateView):
    model = reserva
    fields = '__all__'

class reservaUpdate(UpdateView):
    model = reserva
    fields = ['codigo_reserva', 'fecha_evento', 'nom_cliente', 'apell_cliente',
                'celu_cliente', 'email', 'cant_personas', 'total']

class reservaDelete(DeleteView):
    model = reserva
    success_url = reverse_lazy('index')

class ReservaListView(generic.ListView):
    model = reserva
    paginate_by = 10

class ReservaDetailView(generic.DetailView):
    model = reserva

#Servicios
class servicioCreate(CreateView):
    model = servicio
    fields = '__all__'

class servicioUpdate(UpdateView):
    model = servicio
    fields = ['codigo_servicio', 'nom_servicio', 'descripcion', 'precio_por_persona']

class servicioDelete(DeleteView):
    model = servicio
    success_url = reverse_lazy('index')

class ServicioListView(generic.ListView):
    model = servicio
    paginate_by = 10

class ServicioDetailView(generic.DetailView):
    model = servicio
    
    





