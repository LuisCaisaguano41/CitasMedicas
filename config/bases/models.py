from django.db import models
from django.utils import timezone
from django.utils.http import quote
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UsuarioManager 

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    identificacion = models.CharField(_('cedula'), max_length=10, unique=True)
    first_name = models.CharField(_('nombres'), max_length=40, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=40, blank=True)
    email = models.EmailField(_('direccion email'), max_length=254, unique=True)
    fecha_nac = models.DateField(_('fecha de nacimiento'), blank=True, null=True)
    edad = models.IntegerField(_('edad usuario'), blank=True, null=True)
    genero = models.CharField(_('genero de usuario'), max_length=15, blank=True, null=True)
    ciudad = models.CharField(_('ciudad de usuario'), max_length=50, blank=True, null=True)
    direccion = models.CharField(_('direccion'), max_length=254, blank=True, null=True)
    telefono = models.CharField(_('telefono'), max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(_('es staff'), default=False, help_text=
                                   _('Indica si el usuario puede iniciar sesión en admin'))
    is_active = models.BooleanField(_('activo'), default=True, help_text=
                                   _('Designa si este usuario puede ser tratado como activo'
                                     'Deseleccione esto en lugar de eliminar usuario'))
    fecha_creacion = models.DateTimeField(_('fecha registro'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['identificacion']

    objects = UsuarioManager()

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_absolute_url(self):
        return "/users/%s/" % self.email

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email