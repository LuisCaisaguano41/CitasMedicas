from django.db import models
from datetime import date
from pacientes.models import Paciente
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Triaje(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='triajes')
    fecha_triaje = models.DateTimeField(auto_now_add=True)
    
    frecuencia_cardiaca = models.IntegerField(help_text="Frecuencia cardíaca en latidos por minuto (60-100)", 
                                              validators=[MinValueValidator(60), MaxValueValidator(100)])
    frecuencia_respiratoria = models.IntegerField(help_text="Frecuencia respiratoria en respiraciones por minuto (12-20)", 
                                                  validators=[MinValueValidator(12), MaxValueValidator(20)])
    presion_arterial_min = models.IntegerField(help_text="Presión arterial mínima (80-84 mmHg)", 
                                               validators=[MinValueValidator(80), MaxValueValidator(84)])
    presion_arterial_max = models.IntegerField(help_text="Presión arterial máxima (120-129 mmHg)", 
                                               validators=[MinValueValidator(120), MaxValueValidator(129)])
    temperatura_corporal = models.DecimalField(max_digits=4, decimal_places=1, help_text="Temperatura corporal en grados centígrados (12.0-40.0)", 
                                               validators=[MinValueValidator(12.0), MaxValueValidator(40.0)])
    spo2 = models.DecimalField(max_digits=4, decimal_places=1, help_text="Nivel de saturación de oxígeno en porcentaje (70.0-100.0)", 
                               validators=[MinValueValidator(70.0), MaxValueValidator(100.0)])
    
    prioridad = models.CharField(max_length=50, choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], default='baja')
    estado = models.BooleanField(default=True)
    
    
    
    
    def calcular_prioridad(self):
        if self.frecuencia_cardiaca < 60 or self.frecuencia_cardiaca > 100:
            self.prioridad = 'alta'
        elif self.temperatura_corporal > 38 or self.spo2 < 90:
            self.prioridad = 'alta'
        elif self.presion_arterial_min < 80 or self.presion_arterial_max > 129:
            self.prioridad = 'media'
        else:
            self.prioridad = 'baja'
        return self.prioridad

    def save(self, *args, **kwargs):
        self.calcular_prioridad()
        super(Triaje, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Triajes"