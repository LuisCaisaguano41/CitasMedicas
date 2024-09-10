from django.db import models


# Create your models here.
class Especialidad(models.Model):
    codigo = models.CharField(max_length=10, help_text='Código de la especialidad', unique=True)
    nombre = models.CharField(max_length=50, help_text='Nombre de la especialidad', unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}:{}'.format(self.codigo, self.nombre)
    
    def save(self, *args, **kwargs):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        super(Especialidad, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Especialidades"
        
        


class Medico(models.Model):
    identificacion = models.CharField(max_length=20, unique=True, help_text="Cédula, RUC o Pasaporte")
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=254, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad_residencia = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)  # Campo normal para el género
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"
    
    def save(self, *args, **kwargs):
        self.apellidos = self.apellidos.upper()
        self.nombres = self.nombres.upper()
        super(Medico, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Médicos"
        unique_together = ['identificacion']

        



