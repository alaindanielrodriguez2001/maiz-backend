from rest_framework import serializers
from .models import Campo, Observacion

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo
        fields = ['id', 'nombre_del_campo', 'municipio', 'forma_productiva', 'cultivar', 'tipo_de_suelo', 'sistema_de_riego', 'altura_snm', 'metodo_de_siembra', 'tipo_de_fertilizacion', 'tipo_de_labor_cultural', 'distancia_de_siembra']


class ObservacionSerializer(serializers.ModelSerializer):
    nombre_del_campo = serializers.CharField(source='campo.nombre_del_campo', read_only=True)

    class Meta:
        model = Observacion
        fields = ['id', 'nombre_del_campo', 'fecha', 'fase_fenologica', 'humedad_maxima', 'humedad_minima', 'humedad_media', 'temperatura_maxima', 'temperatura_minima', 'temperatura_media', 'precipitacion', 'presencia_del_hongo']