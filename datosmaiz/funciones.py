from .models import Registro, Unidad, Pronostico

        
#Calcula la suma térmica acumulada de una unidad de cultivo
def calcular_suma_termica(unidad):
    registros = Registro.objects.filter(estacion=unidad.estacion, fecha__gte=unidad.fecha_de_siembra).order_by('fecha')
    suma_termica = 0.0
    for registro in registros:
        temp_max = min(registro.temperatura_maxima, 30)
        temp_min = max(registro.temperatura_minima, 10)
        suma_termica += (temp_max + temp_min) / 2 - 10
    unidad.suma_termica = suma_termica
    unidad.save()
    

#Calcula los días críticos acumulados por una unidad de cultivo
def determinar_dias_criticos(unidad):
    registros = Registro.objects.filter(estacion=unidad.estacion, fecha__gte=unidad.fecha_de_siembra).order_by('fecha')
    dias_criticos = 0
    dias_no_criticos_consecutivos = 0
    for i in range(len(registros) - 7):
        periodo = registros[i:i+7]
        condiciones_cumplidas = all(
            17 <= registro.temperatura_media <= 22 and
            registro.temperatura_maxima < 30 and
            registro.temperatura_minima > 15 and
            registro.horas_hr_mayor_que_90 >= 7 and
            registro.precipitacion > 25
            for registro in periodo
        )
        if condiciones_cumplidas:
            dias_criticos += 1
            dias_no_criticos_consecutivos = 0
        else:
            dias_no_criticos_consecutivos += 1
            if dias_no_criticos_consecutivos > 2:
                dias_criticos = 0
                dias_no_criticos_consecutivos = 0
        if dias_criticos >= 6:
            break
    pronostico = Pronostico.objects.get(unidad=unidad)
    pronostico.dias_criticos = dias_criticos
    pronostico.save()
    

#Actualiza las sumas térmicas y días críticos acumulados
def actualizar_suma_termica_y_dias_criticos():
    unidades = Unidad.objects.all()
    for unidad in unidades:
        calcular_suma_termica(unidad)
        determinar_dias_criticos(unidad)

