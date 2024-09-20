from datetime import date
from django.db import models

class Paciente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, help_text="Cédula, RUC o Pasaporte")
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad_residencia = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)  # Campo normal para el género
    estado = models.BooleanField(default=True)
    
    @property
    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    
    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"
    
    def save(self, *args, **kwargs):
        self.apellidos = self.apellidos.upper()
        self.nombres = self.nombres.upper()
        super(Paciente, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Pacientes"
        unique_together = ['identificacion','correo_electronico']
