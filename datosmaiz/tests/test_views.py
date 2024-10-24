import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from datosmaiz.models import Estacion

@pytest.mark.django_db
def test_estaciones_list():
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('estaciones')
    data = {
        'nombre': 'CSS Ejemplar', 
        'codigo': '076', 
        'municipio' : 'Corralillo'
        }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_estaciones_unauthenticated():
    client = APIClient()
    url = reverse('estaciones')
    data = {'nombre': 'CSS Mala', 'codigo': '077', 'municipio' : 'Corralillo'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
@pytest.mark.django_db
def test_registros_list():
    user = User.objects.create_user(username='testuser', password='testpassword')
    estacion_instance = Estacion.objects.create(
        codigo='763', 
        nombre='Roca Baja', 
        municipio='Sagua La Grande'
    )  
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('registros')
    data = {
        "fecha": "2024-11-09",
        "temperatura_maxima": 23.0,
        "temperatura_minima": 18.0,
        "temperatura_media": 20.5,
        "humedad_maxima": 93.0,
        "humedad_minima": 72.0,
        "humedad_media": 82.5,
        "horas_hr_mayor_que_90": 7.5,
        "hr_mayor_que_90_max": 23.0,
        "hr_mayor_que_90_min": 18.0,
        "hr_mayor_que_90_med": 20.5,
        "precipitacion": 26.8,
        "velocidad_del_viento": 37.0,
        "estacion": estacion_instance.id
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_registros_unauthenticated():
    estacion_instance = Estacion.objects.create(
        codigo='095', 
        nombre='Roca Linda', 
        municipio='Sagua La Grande'
    )   
    client = APIClient()
    url = reverse('registros')
    data = {
        'estacion': estacion_instance, 
        'fecha': '2024-09-03', 
        'temperatura_maxima': 23,
        'temperatura_minima': 20,
        'temperatura_media' : 21.5,
        'humedad_maxima' : 23,
        'humedad_minima' : 20,
        'humedad_media' : 21.5,
        'horas_hr_mayor_que_90' : 5,
        'hr_mayor_que_90_max' : 23,
        'hr_mayor_que_90_min' : 20,
        'hr_mayor_que_90_med' : 21.5,
        'precipitacion' : 56.7,
        'velocidad_del_viento' : 23.3
    }    
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
@pytest.mark.django_db
def test_unidades_list():
    user = User.objects.create_user(username='testuser', password='testpassword')
    estacion_instance = Estacion.objects.create(
        codigo='773', 
        nombre='Piedrecita', 
        municipio='Corralillo'
    )  
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('unidades')
    data = {
        "nombre": "CPA La Nueva Cuba",
        "denominacion_del_cultivar": "Granito bueno",
        "tipo_de_suelo": "Arenoso",
        "fecha_de_siembra": "2024-09-04",
        "semilla_con_tratamiento_quimico": True,
        "area_sembrada": 12.0,
        "tipo_de_fertilizante": "Artificial",
        "dosis_de_fertilizante": 23.0,
        "marco_de_siembra": 2.0,
        "sistema_de_riego": "Natural",
        "suma_termica": 863.5,
        "dias_criticos": 6,
        "estacion": estacion_instance.id
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_unidades_unauthenticated():
    estacion_instance = Estacion.objects.create(
        codigo='195', 
        nombre='CSS Pedrito', 
        municipio='Placetas'
    )   
    client = APIClient()
    url = reverse('unidades')
    data = {
        "nombre": "CPA La Nueva Colombia",
        "denominacion_del_cultivar": "Granito bueno",
        "tipo_de_suelo": "Arenoso",
        "fecha_de_siembra": "2024-09-04",
        "semilla_con_tratamiento_quimico": True,
        "area_sembrada": 12.0,
        "tipo_de_fertilizante": "Artificial",
        "dosis_de_fertilizante": 23.0,
        "marco_de_siembra": 2.0,
        "sistema_de_riego": "Natural",
        "suma_termica": 863.5,
        "dias_criticos": 6,
        "estacion": estacion_instance.id
    }    
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED