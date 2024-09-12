# Generated by Django 5.0.6 on 2024-08-27 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datosmaiz', '0004_estacion_alter_campo_nombre_del_campo_registro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacion',
            name='campo',
        ),
        migrations.AlterModelOptions(
            name='estacion',
            options={'ordering': ['codigo', 'municipio', 'nombre']},
        ),
        migrations.DeleteModel(
            name='Campo',
        ),
        migrations.DeleteModel(
            name='Observacion',
        ),
    ]