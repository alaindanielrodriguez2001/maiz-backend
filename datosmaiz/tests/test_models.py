import pytest
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from datosmaiz.models import Estacion, Unidad, Pronostico, Registro


#Testeo del modelo de usuarios
@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='usuario_test', password='password_test')
    assert user.username == 'usuario_test'
    assert check_password('password_test', user.password)   

#Testeo de modelos
@pytest.mark.django_db
def test_models():
    estacion_instance = Estacion.objects.create(
        codigo='090', 
        nombre='Roca Alta', 
        municipio='Sagua La Grande'
    )   
    assert estacion_instance.codigo == '090'
    assert estacion_instance.nombre == 'Roca Alta'
    assert estacion_instance.municipio == 'Sagua La Grande'

    unidad_instance = Unidad.objects.create(
        nombre ='CPA La Guayaba',
        estacion = estacion_instance,
        denominacion_del_cultivar = 'Chileno',
        tipo_de_suelo = 'Negro',
        fecha_de_siembra = '2024-09-08',
        semilla_con_tratamiento_quimico = True,
        area_sembrada = 456.3,
        tipo_de_fertilizante = 'Natural',
        dosis_de_fertilizante = 23.23,
        marco_de_siembra = 1.2,
        sistema_de_riego = 'Splines'
    )
    assert unidad_instance.estacion == estacion_instance
    assert unidad_instance.nombre == 'CPA La Guayaba'
    assert unidad_instance.denominacion_del_cultivar == 'Chileno'
    assert unidad_instance.tipo_de_suelo == 'Negro'
    assert unidad_instance.fecha_de_siembra == '2024-09-08'
    assert unidad_instance.semilla_con_tratamiento_quimico == True
    assert unidad_instance.area_sembrada == 456.3
    assert unidad_instance.tipo_de_fertilizante == 'Natural'
    assert unidad_instance.dosis_de_fertilizante == 23.23
    assert unidad_instance.marco_de_siembra == 1.2
    assert unidad_instance.sistema_de_riego == 'Splines'

    registro_instance = Registro.objects.create(
        estacion = estacion_instance,
        fecha = '2024-08-08',
        temperatura_maxima = 23,
        temperatura_minima = 20,
        temperatura_media = 21.5,
        humedad_maxima = 23,
        humedad_minima = 20,
        humedad_media = 21.5,
        horas_hr_mayor_que_90 = 5,
        hr_mayor_que_90_max = 23,
        hr_mayor_que_90_min = 20,
        hr_mayor_que_90_med = 21.5,
        precipitacion = 56.7,
        velocidad_del_viento = 23.3
    )
    assert registro_instance.estacion == estacion_instance
    assert registro_instance.fecha == '2024-08-08'
    assert registro_instance.temperatura_maxima == 23
    assert registro_instance.temperatura_minima == 20
    assert registro_instance.temperatura_media == 21.5
    assert registro_instance.humedad_maxima == 23
    assert registro_instance.humedad_minima == 20
    assert registro_instance.humedad_media == 21.5
    assert registro_instance.horas_hr_mayor_que_90 == 5
    assert registro_instance.hr_mayor_que_90_max == 23
    assert registro_instance.hr_mayor_que_90_min == 20
    assert registro_instance.hr_mayor_que_90_med == 21.5
    assert registro_instance.precipitacion == 56.7
    assert registro_instance.velocidad_del_viento == 23.3

    pronostico_instance = Pronostico.objects.create(
        unidad = unidad_instance,
        fecha_de_siembra = '2024-08-08',
        denominacion_del_cultivar = 'Chileno',
        periodo_favorable = '2024-09-09-2024-09-19',
        plazo_primeros_sintomas = '2024-09-19-2024-09-29',
        tipo_de_mensaje = 'Alerta',
        total_grados_dias = 760
    )    
    assert pronostico_instance.unidad == unidad_instance
    assert pronostico_instance.fecha_de_siembra == '2024-08-08'
    assert pronostico_instance.denominacion_del_cultivar == 'Chileno'
    assert pronostico_instance.periodo_favorable == '2024-09-09-2024-09-19'
    assert pronostico_instance.plazo_primeros_sintomas == '2024-09-19-2024-09-29'
    assert pronostico_instance.tipo_de_mensaje == 'Alerta'
    assert pronostico_instance.total_grados_dias == 760

