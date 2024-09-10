from django import forms
from .models import *

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['codigo', 'nombre', 'estado']
        labels = {
            'codigo': "Código",
            'nombre': "Nombre de la Especialidad",
            'estado': "Estado"
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class MedicoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            format='%Y-%m-%d',  # Asegúrate de que el formato coincida con el de tu base de datos
            attrs={'class': 'form-control', 'type': 'date'}
        ),
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Formatos aceptados
    )

    class Meta:
        model = Medico
        fields = [
            'identificacion', 
            'apellidos', 
            'nombres', 
            'correo_electronico', 
            'telefono', 
            'direccion', 
            'ciudad_residencia', 
            'fecha_nacimiento', 
            'genero', 
            'especialidad'  # Relación con el modelo Especialidad
        ]
        labels = {
            'identificacion': "Identificación",
            'apellidos': "Apellidos",
            'nombres': "Nombres",
            'correo_electronico': "Correo Electrónico",
            'telefono': "Teléfono",
            'direccion': "Dirección",
            'ciudad_residencia': "Ciudad de Residencia",
            'fecha_nacimiento': "Fecha de Nacimiento",
            'genero': "Género",
            'especialidad': "Especialidad",
        }
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ciudad_residencia': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),  # Campo de selección para la especialidad
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar la clase 'form-control' a todos los campos del formulario
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['especialidad'].empty_label = "Seleccione especialidad"

