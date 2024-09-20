# forms.py
from django import forms
from .models import Triaje
from pacientes.models import Paciente

class TriajeForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.filter(estado=True),
        required=True,
        label="Paciente"
    )
    
    estado = forms.BooleanField(
        required=False,  # No es obligatorio para manejar el caso cuando no está marcado
        label="Activo"
    )
    
    class Meta:
        model = Triaje
        fields = [
            'paciente',
            'frecuencia_cardiaca',
            'frecuencia_respiratoria',
            'presion_arterial_min',
            'presion_arterial_max',
            'temperatura_corporal',
            'spo2',
            'prioridad',
        ]
        labels = {
            'paciente': "Paciente",
            'frecuencia_cardiaca': "Frecuencia Cardíaca (lpm)",
            'frecuencia_respiratoria': "Frecuencia Respiratoria (rpm)",
            'presion_arterial_min': "Presión Arterial Mínima (mmHg)",
            'presion_arterial_max': "Presión Arterial Máxima (mmHg)",
            'temperatura_corporal': "Temperatura Corporal (°C)",
            'spo2': "Saturación de Oxígeno (%)",
            'prioridad': "Prioridad",
        }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'frecuencia_cardiaca': forms.NumberInput(attrs={'class': 'form-control', 'min': 60, 'max': 100}),
            'frecuencia_respiratoria': forms.NumberInput(attrs={'class': 'form-control', 'min': 12, 'max': 20}),
            'presion_arterial_min': forms.NumberInput(attrs={'class': 'form-control', 'min': 80, 'max': 84}),
            'presion_arterial_max': forms.NumberInput(attrs={'class': 'form-control', 'min': 120, 'max': 129}),
            'temperatura_corporal': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1, 'min': 12.0, 'max': 40.0}),
            'spo2': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1, 'min': 70.0, 'max': 100.0}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar la clase 'form-control' a todos los campos del formulario
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        # Deshabilitar la prioridad porque se calcula automáticamente
        self.fields['prioridad'].disabled = True
