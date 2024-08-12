from django.db import models

class Campo(models.Model):
    nombre_del_campo = models.CharField(max_length=100, unique=True)
    municipio = models.CharField(max_length=100)
    forma_productiva = models.CharField(max_length=100)
    cultivar = models.CharField(max_length=100)
    tipo_de_suelo = models.CharField(max_length=100)
    sistema_de_riego = models.CharField(max_length=100)
    altura_snm = models.IntegerField()
    metodo_de_siembra = models.CharField(max_length=100)
    tipo_de_fertilizacion = models.CharField(max_length=100)
    tipo_de_labor_cultural = models.CharField(max_length=100)
    distancia_de_siembra = models.FloatField()

    class Meta:
        ordering = ['municipio', 'nombre_del_campo']



class Observacion(models.Model):
    campo=models.ForeignKey(Campo, on_delete=models.CASCADE, to_field="id", default=1)
    fecha = models.DateField()
    fase_fenologica = models.IntegerField()
    humedad_maxima = models.FloatField()
    humedad_minima = models.FloatField()
    humedad_media = models.FloatField()
    temperatura_maxima = models.FloatField()
    temperatura_minima = models.FloatField()
    temperatura_media = models.FloatField()
    precipitacion = models.FloatField()
    presencia_del_hongo = models.BooleanField()

    class Meta:
        ordering = ['fecha']

