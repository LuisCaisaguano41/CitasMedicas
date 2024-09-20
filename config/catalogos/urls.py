from django.urls import path
from .views import *

urlpatterns = [

    #Rutas para diagnosticos
    path('diagnosticos/',DiagnosticoView.as_view(), name='diagnostico_list'),
    path('diagnosticos/add',DiagnosticoAdd.as_view(), name='diagnostico_add'),
    path('diagnosticos/update/<int:pk>',DiagnosticoUpdate.as_view(), name='diagnostico_update'),
    #path('activar-desactivar/<str:app_label>/<str:model_name>/<int:id>/', activar_desactivar_diagnostico, name='activar_desactivar_diagnostico'),
    path('diagnosticos/activar-desactivar/<int:id>/', activar_desactivar_diagnostico, name='activar_desactivar_diagnostico'),

    #Rutas para examenes
    path('examenes/',ExamenView.as_view(), name='examen_list'),
    path('examenes/add',ExamenAdd.as_view(), name='examen_add'),
    path('examenes/update/<int:pk>',ExamenUpdate.as_view(), name='examen_update'),
    path('examenes/activar-desactivar/<int:id>/', activar_desactivar_examen, name='activar_desactivar_examen'),

     #Rutas para medicamentos
    path('medicamentos/',MedicamentoView.as_view(), name='medicamento_list'),
    path('medicamentos/add',MedicamentoAdd.as_view(), name='medicamento_add'),
    path('medicamentos/update/<int:pk>',MedicamentoUpdate.as_view(), name='medicamento_update'),
    path('medicamentos/activar-desactivar/<int:id>/', activar_desactivar_medicamento, name='activar_desactivar_medicamento'),
]