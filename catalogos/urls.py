from django.urls import path
from .views import *

urlpatterns = [

    #Rutas para diagnosticos
    path('diagnosticos/',DiagnosticoView.as_view(), name='diagnostico_list'),
    path('diagnosticos/add',DiagnosticoAdd.as_view(), name='diagnostico_add'),
    path('diagnosticos/update/<int:pk>',DiagnosticoUpdate.as_view(), name='diagnostico_update'),
    path('diagnosticos/activar-desactivar/<int:id>/', activar_desactivar_diagnostico, name='activar_desactivar_diagnostico'),

]