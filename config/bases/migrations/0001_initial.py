# Generated by Django 4.2.13 on 2024-06-28 03:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('identificacion', models.CharField(max_length=10, unique=True, verbose_name='cedula')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='nombres')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='direccion email')),
                ('fecha_nac', models.DateField(blank=True, verbose_name='fecha de nacimiento')),
                ('edad', models.IntegerField(blank=True, verbose_name='edad usuario')),
                ('genero', models.CharField(blank=True, max_length=15, verbose_name='genero de usuario')),
                ('ciudad', models.CharField(blank=True, max_length=50, verbose_name='ciudad de usuario')),
                ('direccion', models.CharField(blank=True, max_length=254, verbose_name='direccion')),
                ('telefono', models.CharField(blank=True, max_length=10, verbose_name='telefono')),
                ('staff', models.BooleanField(default=False, help_text='Indica si el usuario puede iniciar sesión en admin', verbose_name='es staff')),
                ('estado', models.BooleanField(default=True, help_text='Designa si este usuario puede ser tratado como activoDeseleccione esto en lugar de eliminar usuario', verbose_name='activo')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha registro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]
