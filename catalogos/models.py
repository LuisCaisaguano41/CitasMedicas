from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    codigo = models.CharField(max_length=10, help_text='Rango del Personal', unique=True)
    nombre = models.CharField(max_length=50, help_text='Rango del Personal', unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.codigo)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Diagnostico, self).save()

    class Meta:
        verbose_name_plural = "Diagnosticos"
