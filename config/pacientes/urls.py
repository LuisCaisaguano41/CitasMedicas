from django.urls import path
from .views import *

urlpatterns = [
    
    #Rutas para Pacientes
    path('list/',PacientesView.as_view(), name='pacientes_list'),
    path('add/',PacientesAdd.as_view(), name='pacientes_add'),
    path('update/<int:pk>',PacientesUpdate.as_view(), name='pacientes_update'),
    path('activar-desactivar/<int:id>/', activar_desactivar_pacientes, name='activar_desactivar_pacientes'),
]
