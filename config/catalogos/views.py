from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Vista para listar o ver diagnosticos
class DiagnosticoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/diagnostico_list.html"
    model = Diagnostico
    context_object_name = "obj"

# Vista de para crear diagnosticos
class DiagnosticoAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/diagnostico_form.html"
    login_url = 'bases:login'
    model = Diagnostico
    form_class = DiagnosticoForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:diagnostico_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar Diagnosticos
class DiagnosticoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/diagnostico_form.html"
    login_url = 'bases:login'
    form_class = DiagnosticoForm
    model = Diagnostico
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:diagnostico_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
#vista de funciones para activar y desactivar diagnosticos
def activar_desactivar_diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, pk=id)

    if request.method == 'POST':
        diagnostico.estado = not diagnostico.estado  # Invertimos el estado actual
        diagnostico.save()

        return JsonResponse({'estado': diagnostico.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST


# Vista para listar o ver examenes
class ExamenView(LoginRequiredMixin, ListView):
    template_name = "catalogos/examen_list.html"
    login_url = 'bases:login'
    model = Examen
    context_object_name = "obj"

# Vista de para crear examenes
class ExamenAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/examen_form.html"
    login_url = 'bases:login'
    model = Examen
    form_class = ExamenForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:examen_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar examenes
class ExamenUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/examen_form.html"
    login_url = 'bases:login'
    form_class = ExamenForm
    model = Examen
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:examen_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
#vista de funciones para activar y desactivar examenes
def activar_desactivar_examen(request, id):
    examen = get_object_or_404(Examen, pk=id)

    if request.method == 'POST':
        examen.estado = not examen.estado  # Invertimos el estado actual
        examen.save()

        return JsonResponse({'estado': examen.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST


# Vista para listar o ver medicamentos
class MedicamentoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/medicamento_list.html"
    login_url = 'bases:login'
    model = Medicamento
    context_object_name = "obj"

# Vista de para crear medicamentos
class MedicamentoAdd(LoginRequiredMixin, CreateView):
    template_name = "catalogos/medicamento_form.html"
    login_url = 'bases:login'
    model = Medicamento
    form_class = MedicamentoForm
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:medicamento_list")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
# Vista de clase para editar medicamento
class MedicamentoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "catalogos/medicamento_form.html"
    login_url = 'bases:login'
    form_class = MedicamentoForm
    model = Medicamento
    context_object_name = "obj"
    success_url = reverse_lazy("catalogos:medicamento_list")
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
#vista de funciones para activar y desactivar medicamentos
def activar_desactivar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, pk=id)

    if request.method == 'POST':
        medicamento.estado = not medicamento.estado  # Invertimos el estado actual
        medicamento.save()

        return JsonResponse({'estado': medicamento.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST