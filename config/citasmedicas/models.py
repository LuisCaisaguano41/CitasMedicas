from django.db import models
from datetime import date
from catalogos.models import *
from pacientes.models import *
from gestionmedica.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import time

class CitaMedica(models.Model):
    hora = models.CharField(max_length=5)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=50)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, null=True, blank=True)
    examenes = models.ManyToManyField(Examen, blank=True)
    estado = models.BooleanField(default=True)
    
    @property
    def edad(self):
        today = date.today()
        return today.year - self.paciente.fecha_nacimiento.year - ((today.month, today.day) < (self.paciente.fecha_nacimiento.month, self.paciente.fecha_nacimiento.day))
    
    def clean(self):
        """Validación adicional para asegurar que la hora está en el formato y franja adecuada."""
        try:
            # Validación del formato de la hora: Debe estar en HH:MM
            hora_format = timezone.datetime.strptime(self.hora, '%H:%M').time()
            
            # Validación de franjas horarias
            if not ((timezone.time(9, 0) <= hora_format <= timezone.time(12, 0)) or 
                    (timezone.time(16, 0) <= hora_format <= timezone.time(18, 0))):
                raise ValidationError("La hora de la cita debe estar dentro de las franjas 09:00-12:00 o 16:00-18:00.")
        except ValueError:
            raise ValidationError("El formato de la hora debe ser HH:MM.")
    
    def save(self, *args, **kwargs):
        """Sobrescribe el método save para aplicar validaciones personalizadas y formatear datos."""
        # Convertir el motivo a mayúsculas
        self.motivo = self.motivo.upper()
        
        # Realizar la validación antes de guardar
        self.clean()
        
        # Llamar al método save original
        super(CitaMedica, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Citas Médicas"
        unique_together = ['hora', 'medico', 'paciente']  # Un médico no puede tener dos citas a la misma hora con diferentes pacientes
