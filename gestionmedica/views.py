from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *

# Create para listar o llamar a las especialidades
class EspecialidadesView(LoginRequiredMixin, ListView):
    template_name = "gestionmedica/especialidad_list.html"
    login_url = 'bases:login'
    model = Especialidad
    context_object_name = "obj"

# Vista de para crear especialidades
class EspecialidadesAdd(LoginRequiredMixin, CreateView):
    template_name = "gestionmedica/especialidad_form.html"
    login_url = 'bases:login'
    model = Especialidad
    form_class = EspecialidadForm
    context_object_name = "obj"
    success_url = reverse_lazy("gestionmedica:especialidades_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

# Vista para editar especialidades
class EspecialidadesUpdate(LoginRequiredMixin, UpdateView):
    template_name = "gestionmedica/especialidad_form.html"
    login_url = 'bases:login'
    form_class = EspecialidadForm
    model = Especialidad
    context_object_name = "obj"
    success_url = reverse_lazy("gestionmedica:especialidades_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
#vista de funciones para activar y desactivar especialidades
def activar_desactivar_especialidades(request, id):
    especialidad = get_object_or_404(Especialidad, pk=id)

    if request.method == 'POST':
        especialidad.estado = not especialidad.estado  # Invertimos el estado actual
        especialidad.save()

        return JsonResponse({'estado': especialidad.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST

# Create para listar o llamar a medicos
class MedicosView(LoginRequiredMixin, ListView):
    template_name = "gestionmedica/medico_list.html"
    login_url = 'bases:login'
    model = Medico
    context_object_name = "obj"
    
# Vista de para crear especialidades
class MedicoAdd(LoginRequiredMixin, CreateView):
    template_name = "gestionmedica/medico_form.html"
    login_url = 'bases:login'
    model = Medico
    form_class = MedicoForm
    context_object_name = "obj"
    success_url = reverse_lazy("gestionmedica:medicos_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.filter(estado=True).order_by('nombre')
        return context
    
#Vista para editar medicos
class MedicoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "gestionmedica/medico_form.html"
    login_url = 'bases:login'
    model = Medico
    form_class = MedicoForm
    context_object_name = "obj"
    success_url = reverse_lazy("gestionmedica:medicos_list")

    def form_valid(self, form):
        form.instance.um = self.request.user  # Actualiza el usuario que modifica
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = Especialidad.objects.filter(estado=True).order_by('nombre')
        return context
    

#vista de funciones para activar y desactivar medicos
def activar_desactivar_medicos(request, id):
    medico = get_object_or_404(Medico, pk=id)

    if request.method == 'POST':
        medico.estado = not medico.estado  # Invertimos el estado actual
        medico.save()

        return JsonResponse({'estado': medico.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST
