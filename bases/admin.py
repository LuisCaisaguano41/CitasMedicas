from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'first_name', 'last_name', 'fecha_nac', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('identificacion', 'first_name', 'last_name', 'fecha_nac', 'edad', 'genero', 'ciudad', 'direccion', 'telefono')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'fecha_creacion')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    form = UserChangeForm
    add_form = UserCreationForm
    
    search_fields = ('email', 'first_name', 'last_name', 'identificacion')
    ordering = ('email',)

admin.site.register(Usuario, UsuarioAdmin)




