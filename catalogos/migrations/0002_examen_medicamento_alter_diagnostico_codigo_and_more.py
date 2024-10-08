# Generated by Django 4.2.13 on 2024-07-12 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Codigo de examen', max_length=10, unique=True)),
                ('nombre', models.CharField(help_text='Nombre del examen', max_length=50, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Examenes',
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Codigo de medicamento', max_length=10, unique=True)),
                ('nombre', models.CharField(help_text='Nombre del medicamento', max_length=50, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Medicamentos',
            },
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='codigo',
            field=models.CharField(help_text='Codigo del diagnostico', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='nombre',
            field=models.CharField(help_text='Nombre del diagnostico', max_length=50, unique=True),
        ),
    ]
