# Generated by Django 4.2.13 on 2024-06-28 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de nacimiento'),
        ),
    ]
