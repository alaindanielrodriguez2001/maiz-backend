# Generated by Django 5.0.6 on 2024-09-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosmaiz', '0005_remove_observacion_campo_alter_estacion_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pronostico',
            name='fase_fenologica',
        ),
        migrations.AddField(
            model_name='pronostico',
            name='dias_criticos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unidad',
            name='suma_termica',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterUniqueTogether(
            name='registro',
            unique_together={('estacion', 'fecha')},
        ),
    ]
