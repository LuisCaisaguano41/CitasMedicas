from django import forms
from .models import *

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['codigo','nombre','estado']
        labels = {'codigo':"Codigo",'nombre':"Nombre diagnosticos",'estado':"Estado"}
        widget = {'codigo': forms.TextInput, 'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['codigo','nombre','estado']
        labels = {'codigo':"Codigo",'nombre':"Nombre examenes",'estado':"Estado"}
        widget = {'codigo': forms.TextInput, 'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['codigo','nombre','estado']
        labels = {'codigo':"Codigo",'nombre':"Nombre medicamentos",'estado':"Estado"}
        widget = {'codigo': forms.TextInput, 'nombre': forms.TextInput}

    def __ini__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })