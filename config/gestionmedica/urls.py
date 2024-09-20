from django.urls import path
from .views import *

urlpatterns = [
    
    #Rutas para Especialidades
    path('especialidades/',EspecialidadesView.as_view(), name='especialidades_list'),
    path('especialidades/add',EspecialidadesAdd.as_view(), name='especialidades_add'),
    path('especialidades/update/<int:pk>',EspecialidadesUpdate.as_view(), name='especialidades_update'),
    path('especialidades/activar-desactivar/<int:id>/', activar_desactivar_especialidades, name='activar_desactivar_especialidades'),
    
    #Rutas para Medicos
    path('medicos/',MedicosView.as_view(), name='medicos_list'),
    path('medicos/add',MedicoAdd.as_view(), name='medicos_add'),
    path('medicos/update/<int:pk>',MedicoUpdate.as_view(), name='medicos_update'),
    path('medicos/activar-desactivar/<int:id>/', activar_desactivar_medicos, name='activar_desactivar_medicos'),
]
