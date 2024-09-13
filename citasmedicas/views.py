from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.utils import timezone
from .forms import *
from .models import *
from django.urls import reverse_lazy

# Create para listar o llamar a pacientes
class CitasMedicasView(LoginRequiredMixin, ListView):
    template_name = "citasmedicas/citamedica_list.html"
    login_url = 'bases:login'
    model = CitaMedica
    context_object_name = "obj"