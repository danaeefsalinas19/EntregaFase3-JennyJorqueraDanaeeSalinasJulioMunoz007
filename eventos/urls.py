from django.urls import path
from . import views
from django.urls import reverse_lazy



urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('descEventos/', views.descEventos, name='descEventos'),
    path('reservas/', views.reservas, name='reservas'),
    path('listado/', views.ReservaListView.as_view(), name ='listado'),
    path('reserva/<int:pk>', views.ReservaDetailView.as_view(), name='reserva_detalle'),
    path('servicio/<int:pk>', views.ServicioDetailView.as_view(), name='servicio_detalle'),
    path('listado2/', views.ServicioListView.as_view(), name ='listado2'),
]

urlpatterns += [
    path('reserva/create/', views.reservaCreate.as_view(), name='reserva_create'),
    path('reserva/<str:pk>/update/', views.reservaUpdate.as_view(), name='update'),
    path('reserva/<str:pk>/delete/', views.reservaDelete.as_view(), name='delete'),
    path('servicio/create/', views.servicioCreate.as_view(), name='servicio_create'),
    path('servicio/<str:pk>/update/', views.servicioUpdate.as_view(), name='update'),
    path('servicio/<str:pk>/delete/', views.servicioDelete.as_view(), name='delete'),
]

