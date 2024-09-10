from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

# Create para listar o llamar a pacientes
class PacientesView(LoginRequiredMixin, ListView):
    template_name = "pacientes/paciente_list.html"
    login_url = 'bases:login'
    model = Paciente
    context_object_name = "obj"
    
class PacientesAdd(LoginRequiredMixin, CreateView):
    template_name = "pacientes/paciente_form.html"
    login_url = 'bases:login'
    model = Paciente
    form_class = PacienteForm
    context_object_name = "obj"
    success_url = reverse_lazy("pacientes:pacientes_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    
    
#Vista para editar pacientes
class PacientesUpdate(LoginRequiredMixin, UpdateView):
    template_name = "pacientes/pacientes_form.html"
    login_url = 'bases:login'
    model = Paciente
    form_class = PacienteForm
    context_object_name = "obj"
    success_url = reverse_lazy("pacientes:pacientes_list")

    def form_valid(self, form):
        form.instance.um = self.request.user  # Actualiza el usuario que modifica
        return super().form_valid(form)
    
#vista de funciones para activar y desactivar pacientes
def activar_desactivar_pacientes(request, id):
    paciente = get_object_or_404(Paciente, pk=id)

    if request.method == 'POST':
        paciente.estado = not paciente.estado  # Invertimos el estado actual
        paciente.save()

        return JsonResponse({'estado': paciente.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST
