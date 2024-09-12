from django.db import models

class Estacion(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100, unique = True)
    municipio = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['codigo', 'municipio', 'nombre']
        
class Registro(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, to_field="id", default=1)
    fecha = models.DateField()
    temperatura_maxima = models.FloatField()
    temperatura_minima = models.FloatField()
    temperatura_media = models.FloatField()
    humedad_maxima = models.FloatField()
    humedad_minima = models.FloatField()
    humedad_media = models.FloatField()
    horas_hr_mayor_que_90 = models.FloatField()
    hr_mayor_que_90_max = models.FloatField()
    hr_mayor_que_90_min = models.FloatField()
    hr_mayor_que_90_med = models.FloatField()
    precipitacion = models.FloatField()
    velocidad_del_viento = models.FloatField()

    class Meta:
        ordering = ['fecha']
        unique_together = ['estacion', 'fecha']


    
class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE, to_field="id", default=1)
    denominacion_del_cultivar = models.CharField(max_length=100)
    tipo_de_suelo = models.CharField(max_length=100)
    fecha_de_siembra = models.DateField()
    semilla_con_tratamiento_quimico = models.BooleanField()
    area_sembrada = models.FloatField()
    tipo_de_fertilizante = models.CharField(max_length=100)
    dosis_de_fertilizante = models.FloatField()
    marco_de_siembra = models.FloatField()
    sistema_de_riego = models.CharField(max_length=100)
    
    #Para la emisión de pronósticos
    suma_termica = models.FloatField(default=0.0)
    
    class Meta:
        ordering = ['nombre']
    
    
class Pronostico(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, to_field="id", default=1)
    denominacion_del_cultivar = models.CharField(max_length=100)
    periodo_favorable = models.IntegerField()
    plazo_primeros_sintomas = models.IntegerField()
    tipo_de_mensaje = models.CharField(max_length=100)
    total_grados_dias = models.FloatField()
    
    #Conteo de días críticos
    dias_criticos = models.IntegerField(default=0)
    class Meta:
        ordering = ['unidad']


