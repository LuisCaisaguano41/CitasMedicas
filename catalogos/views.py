from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Diagnostico
from .forms import DiagnosticoForm
from django.urls import reverse_lazy


# Vista para listar o ver diagnosticos
class DiagnosticoView(LoginRequiredMixin, ListView):
    template_name = "catalogos/diagnostico_list.html"
    login_url = 'bases:login'
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
    
def activar_desactivar_diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, pk=id)

    if request.method == 'POST':
        diagnostico.estado = not diagnostico.estado  # Invertimos el estado actual
        diagnostico.save()

        return JsonResponse({'estado': diagnostico.estado})  # Devolvemos el estado actualizado como JSON

    return JsonResponse({'error': 'Método no permitido'}, status=405)  # Método no permitido si no es POST