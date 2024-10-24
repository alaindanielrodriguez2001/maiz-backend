from django.urls import reverse, resolve

def test_url_resolves_to_estaciones():
    url = reverse('estaciones')
    assert resolve(url).view_name == 'estaciones'
    
def test_url_resolves_to_registros():
    url = reverse('registros')
    assert resolve(url).view_name == 'registros'
    
def test_url_resolves_to_unidades():
    url = reverse('unidades')
    assert resolve(url).view_name == 'unidades'
    
def test_url_resolves_to_pronosticos():
    url = reverse('pronosticos')
    assert resolve(url).view_name == 'pronosticos'
