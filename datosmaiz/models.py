from django.db import models

#Modelo para almacenar los datos de las estaciones meteorológicas
class Estacion(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100, unique = True)
    municipio = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['codigo', 'municipio', 'nombre']
        
#Modelo para almacenar las observaciones diarias de las estaciones meteorológicas
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
        ordering = ['-fecha']
        unique_together = ['estacion', 'fecha']


#Modelo para almacenar los datos de las unidades de cultivo
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
    dias_criticos = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['nombre']
    
#Modelo para almacenar los pronósticos emitidos
class Pronostico(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, to_field="id", default=1)
    fecha_de_siembra = models.DateField(null=True)
    denominacion_del_cultivar = models.CharField(max_length=100)
    periodo_favorable = models.CharField(max_length=100)
    plazo_primeros_sintomas = models.CharField(max_length=100)
    tipo_de_mensaje = models.CharField(max_length=100)
    total_grados_dias = models.FloatField()

    class Meta:
        ordering = ['unidad']
        unique_together = ['unidad', 'fecha_de_siembra', 'denominacion_del_cultivar', 'tipo_de_mensaje']


