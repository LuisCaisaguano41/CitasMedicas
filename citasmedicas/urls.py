from django.urls import path
from .views import *


urlpatterns = [
    #Rutas para citas medicas
    path('list/',CitasMedicasView.as_view(), name='citasmedicas_list'),
]