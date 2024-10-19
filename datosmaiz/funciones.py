from .models import Registro, Unidad, Pronostico
from datetime import timedelta

        
#Calcula la suma térmica acumulada de una unidad de cultivo
def calcular_suma_termica(unidad):
    registros = Registro.objects.filter(estacion=unidad.estacion, fecha__gte = unidad.fecha_de_siembra).order_by('fecha')
    suma_termica = 0.0
    for registro in registros:
        temp_max = min(registro.temperatura_maxima, 30)
        temp_min = max(registro.temperatura_minima, 10)
        suma_termica += (temp_max + temp_min) / 2 - 10
    unidad.suma_termica = suma_termica
    unidad.save()
    

#Calcula los días críticos acumulados por una unidad de cultivo
def determinar_dias_criticos(unidad):
    registros = Registro.objects.filter(estacion = unidad.estacion, fecha__gte = unidad.fecha_de_siembra).order_by('fecha')
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
    unidad.dias_criticos = dias_criticos
    unidad.save()
    

#Emite los pronósticos de advertencia
def emitir_pronosticos():
    unidades = Unidad.objects.all()
    
    for unidad in unidades:
        calcular_suma_termica(unidad)
        determinar_dias_criticos(unidad)
        
        if unidad.dias_criticos >= 5:
            # Obtiene el último día crítico registrado
            registros = Registro.objects.filter(estacion=unidad.estacion, fecha__gte=unidad.fecha_de_siembra).order_by('fecha')
            ultimo_dia_critico = registros[len(registros) - 1].fecha
            
            # Calcula las fechas para periodo_favorable y plazo_primeros_sintomas
            fecha_inicio_periodo_favorable = (ultimo_dia_critico - timedelta(days=10)).strftime('%d/%m/%Y')
            fecha_fin_periodo_favorable = ultimo_dia_critico.strftime('%d/%m/%Y')
            periodo_favorable = f"{fecha_inicio_periodo_favorable}-{fecha_fin_periodo_favorable}"
            
            fecha_inicio_plazo_sintomas = ultimo_dia_critico.strftime('%d/%m/%Y')
            fecha_fin_plazo_sintomas = (ultimo_dia_critico + timedelta(days=10)).strftime('%d/%m/%Y')
            plazo_primeros_sintomas = f"{fecha_inicio_plazo_sintomas}-{fecha_fin_plazo_sintomas}"
            
            # Determina el tipo de mensaje
            if unidad.dias_criticos == 5:
                tipo_de_mensaje = "Alerta"
            else:
                tipo_de_mensaje = "Peligro máximo"
            
            # Crea y guarda el nuevo pronóstico
            pronostico = Pronostico(
                unidad=unidad,
                fecha_de_siembra = unidad.fecha_de_siembra,
                denominacion_del_cultivar=unidad.denominacion_del_cultivar,
                periodo_favorable=periodo_favorable,
                plazo_primeros_sintomas=plazo_primeros_sintomas,
                tipo_de_mensaje=tipo_de_mensaje,
                total_grados_dias=unidad.suma_termica
            )
            try:
                pronostico.save()
            except Exception as e:
                pass
            


            
        


