from rest_framework import serializers
from .models import Estacion, Registro, Unidad, Pronostico
from django.contrib.auth.models import User

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    estacion_codigo = serializers.CharField(source='estacion.codigo', read_only=True)
    class Meta:
        model = Registro
        fields = '__all__'       
 
class UnidadSerializer(serializers.ModelSerializer):
    estacion_codigo = serializers.CharField(source='estacion.codigo', read_only=True)
    class Meta: 
        model = Unidad
        fields = '__all__'
        
class PronosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronostico
        fields = '__all__'
    
        

#Relacionado con la autenticaci'on
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user