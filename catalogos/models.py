from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    codigo = models.CharField(max_length=10, help_text='Codigo del diagnostico', unique=True)
    nombre = models.CharField(max_length=50, help_text='Nombre del diagnostico', unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.codigo, self.nombre)
    
    def save(self):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        super(Diagnostico, self).save()

    class Meta:
        verbose_name_plural = "Diagnosticos"


class Examen(models.Model):
    codigo = models.CharField(max_length=10, help_text='Codigo de examen', unique=True)
    nombre = models.CharField(max_length=50, help_text='Nombre del examen', unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.codigo, self.nombre)
    
    def save(self):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        super(Examen, self).save()

    class Meta:
        verbose_name_plural = "Examenes"

class Medicamento(models.Model):
    codigo = models.CharField(max_length=10, help_text='Codigo de medicamento', unique=True)
    nombre = models.CharField(max_length=50, help_text='Nombre del medicamento', unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.codigo, self.nombre)
    
    def save(self):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        super(Medicamento, self).save()

    class Meta:
        verbose_name_plural = "Medicamentos"
