from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import *
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Listar triaje
class TriajeView(LoginRequiredMixin, ListView):
    template_name = "triaje/triaje_list.html"
    login_url = 'bases:login'
    model = Triaje
    context_object_name = "obj"
    
# Crear triaje
class TriajeAdd(LoginRequiredMixin, CreateView):
    template_name = "triaje/triaje_form.html"
    login_url = 'bases:login'
    model = Triaje
    form_class = TriajeForm
    context_object_name = "obj"
    success_url = reverse_lazy("triajes:triaje_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.filter(estado=True).order_by('nombres')
        return context
    
#Editar triaje
class TriajeUpdate(LoginRequiredMixin, UpdateView):
    template_name = "triaje/triaje_form.html"
    login_url = 'bases:login'
    model = Triaje
    form_class = TriajeForm
    context_object_name = "obj"
    success_url = reverse_lazy("triajes:triaje_list")

    def form_valid(self, form):
        # Actualiza el usuario que modifica
        form.instance.um = self.request.user
        # Forzamos la actualización de prioridad, aunque el campo esté deshabilitado
        triaje = form.save(commit=False)
        triaje.prioridad = triaje.calcular_prioridad()  # Calcula la prioridad nuevamente
        triaje.save()  # Guarda manualmente
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pasa los pacientes activos al contexto
        context['pacientes'] = Paciente.objects.filter(estado=True).order_by('nombres')
        return context
    
#vista de funciones para activar y desactivar triaje
def activar_desactivar_triaje(request, id):
    triaje = get_object_or_404(Triaje, pk=id)

    if request.method == 'POST':
        triaje.estado = not triaje.estado  # Invertimos el estado actual
        triaje.save()

        return JsonResponse({'estado': Triaje.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST
