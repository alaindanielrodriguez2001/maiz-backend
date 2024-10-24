import pytest
from datosmaiz.serializers import EstacionSerializer, RegistroSerializer
from datosmaiz.models import Estacion

@pytest.mark.django_db
def test_valid_Estacion_serializer():
    valid_data = {'nombre': 'CSS Constructiva', 'codigo': '098', 'municipio' : 'Corralillo'}
    serializer = EstacionSerializer(data=valid_data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_invalid_Estacion_serializer():
    invalid_data = {'name': '', 'value': 100}
    serializer = EstacionSerializer(data=invalid_data)
    assert not serializer.is_valid()
    
@pytest.mark.django_db
def test_valid_Registro_serializer():
    estacion_instance = Estacion.objects.create(
        codigo='185', 
        nombre='CSS Juanito', 
        municipio='Placetas'
    ) 
    valid_data = {
        "fecha": "2024-12-08",
        "temperatura_maxima": 18.2,
        "temperatura_minima": 17.8,
        "temperatura_media": 18.0,
        "humedad_maxima": 96.0,
        "humedad_minima": 74.0,
        "humedad_media": 85.0,
        "horas_hr_mayor_que_90": 10.3,
        "hr_mayor_que_90_max": 18.2,
        "hr_mayor_que_90_min": 17.8,
        "hr_mayor_que_90_med": 18.0,
        "precipitacion": 29.0,
        "velocidad_del_viento": 26.0,
        "estacion": estacion_instance.id
        }
    serializer = RegistroSerializer(data=valid_data)
    assert serializer.is_valid()
    
@pytest.mark.django_db
def test_invalid_Registro_serializer():
    invalid_data = {'name': '', 'value': 100}
    serializer = RegistroSerializer(data=invalid_data)
    assert not serializer.is_valid()