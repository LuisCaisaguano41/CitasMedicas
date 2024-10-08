# Generated by Django 4.2.13 on 2024-06-28 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0002_alter_usuario_fecha_nac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ciudad de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(blank=True, null=True, verbose_name='edad usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='genero de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='telefono'),
        ),
    ]
