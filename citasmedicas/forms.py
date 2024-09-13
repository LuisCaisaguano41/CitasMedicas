from django import forms
from django.utils import timezone
from .models import CitaMedica
from datetime import time

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['hora', 'especialidad', 'medico', 'paciente', 'motivo', 'diagnostico', 'examenes', 'estado']
        widgets = {
            'hora': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motivo de la cita'}),
            'diagnostico': forms.Select(attrs={'class': 'form-control'}),
            'examenes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def clean_hora(self):
        """Validación adicional para la hora dentro del formulario."""
        hora = self.cleaned_data.get('hora')
        hora_format = timezone.datetime.strptime(hora, '%H:%M').time()
        
        if not ((timezone.time(9, 0) <= hora_format <= timezone.time(12, 0)) or
                (timezone.time(16, 0) <= hora_format <= timezone.time(18, 0))):
            raise forms.ValidationError("La hora de la cita debe estar dentro de las franjas 09:00-12:00 o 16:00-18:00.")
        return hora
