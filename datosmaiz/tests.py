import pytest
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status
from datosmaiz.models import Estacion
from datosmaiz.serializers import EstacionSerializer

#Testeo de modelos
@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='usuario_test', password='password_test')
    assert user.username == 'usuario_test'
    assert check_password('password_test', user.password)

@pytest.mark.django_db
def test_Estacion():
    estacion = Estacion.objects.create(codigo='090', nombre='Roca Alta', municipio='Sagua La Grande')
    assert estacion.codigo == '090'
    assert estacion.nombre == 'Roca Alta'
    assert estacion.municipio == 'Sagua La Grande'
    

#Testeo de views
@pytest.mark.django_db
def test_estaciones_list():
    user = User.objects.create_user('testuser', 'testpassword')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('estaciones')
    data = {'nombre': 'CSS Ejemplar', 'codigo': '076', 'municipio' : 'Corralillo'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_my_view_unauthenticated():
    client = APIClient()
    url = reverse('estaciones')
    data = {'nombre': 'CSS Ejemplar', 'codigo': '076', 'municipio' : 'Corralillo'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

#Testeo de serializadores
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


#Testeo de URLs
def test_url_resolves_to_estaciones():
    url = reverse('estaciones')
    assert resolve(url).view_name == 'estaciones'
    
def test_url_resolves_to_registros():
    url = reverse('registros')
    assert resolve(url).view_name == 'registros'
