from django.urls import path
from .views import *

urlpatterns = [
    
    #Rutas para Pacientes
    path('list/',TriajeView.as_view(), name='triaje_list'),
    path('add/',TriajeAdd.as_view(), name='triaje_add'),
    path('update/<int:pk>',TriajeUpdate.as_view(), name='triaje_update'),
    path('triaje/activar-desactivar/<int:id>/', activar_desactivar_triaje, name='activar_desactivar_triaje'),
]