# Generated by Django 5.0.6 on 2024-07-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosmaiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('fase_fenologica', models.IntegerField()),
                ('humedad_maxima', models.FloatField()),
                ('humedad_minima', models.FloatField()),
                ('humedad_media', models.FloatField()),
                ('temperatura_maxima', models.FloatField()),
                ('temperatura_minima', models.FloatField()),
                ('temperatura_media', models.FloatField()),
                ('precipitacion', models.FloatField()),
                ('presencia_del_hongo', models.BooleanField()),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]