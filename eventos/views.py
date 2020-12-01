from django.shortcuts import render
from . models import reserva, servicio
from django.views import generic

#importamos información para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    num_servicio = servicio.objects.all()
   
    return render(
        request,
        'index.html',
        context={'num_servicio': num_servicio},
    )


def eventos(request):
    
    num_servicio = servicio.objects.all()
    return render(
        request,
        'eventos.html',
        context={'num_servicio': num_servicio},
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
    fields = ['id', 'fecha_del_evento', 'Servicio', 'Nombre',
                'Apellido', 'Celular', 'Email', 'Cantidad_de_personas','Comentarios']

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
    num_servicio = servicio.objects.all()
    context={'num_servicio': num_servicio},
    model = servicio
    fields = '__all__'

class servicioUpdate(UpdateView):
    model = servicio
    fields = ['id', 'nom_servicio', 'precio_por_persona']

class servicioDelete(DeleteView):
    model = servicio
    success_url = reverse_lazy('index')

class ServicioListView(generic.ListView):
    model = servicio
    paginate_by = 10

class ServicioDetailView(generic.DetailView):
    model = servicio
    
    





