from django import forms
from .models import Diagnostico

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