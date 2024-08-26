from .models import Campo, Observacion, Estacion, Registro, Unidad, Pronostico
from .serializers import CampoSerializer, ObservacionSerializer, EstacionSerializer, RegistroSerializer, UnidadSerializer, PronosticoSerializer, RegisterSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

#Views viejas

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def observaciones_list(request):
    if request.method == 'GET':
        observaciones = Observacion.objects.all().order_by('-fecha')
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ObservacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def observacion(request, pk):
    if request.method == 'GET':
        observacion = Observacion.objects.get(id=pk)
        serializer = ObservacionSerializer(observacion)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        observacion = Observacion.objects.get(id=pk)
        observacion.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def campos_list(request):
    if request.method == 'GET':
        campos = Campo.objects.all()
        serializer = CampoSerializer(campos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CampoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def campo(request, pk):
    if request.method == 'GET':
        campo = Campo.objects.get(id=pk)
        serializer = CampoSerializer(campo)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        campo = Campo.objects.get(id=pk)
        campo.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def observaciones_de_un_campo(request, campo_pk):
    try:
        if campo_pk == 0:
            observaciones = Observacion.objects.all()
        else:
            observaciones = Observacion.objects.filter(campo_id=campo_pk)
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)
    except Campo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Observacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
#Views nuevas

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def estaciones_list(request):
    if request.method == 'GET':
        estaciones = Estacion.objects.all()
        serializer = EstacionSerializer(estaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EstacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def estacion(request, pk):
    if request.method == 'GET':
        estacion = Estacion.objects.get(id=pk)
        serializer = EstacionSerializer(estacion)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        estacion = Estacion.objects.get(id=pk)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def registros_list(request):
    if request.method == 'GET':
        registros = Registro.objects.all().order_by('-fecha')
        serializer = RegistroSerializer(registros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def registro(request, pk):
    if request.method == 'GET':
        registro = Registro.objects.get(id=pk)
        serializer = RegistroSerializer(registro)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        registro = Registro.objects.get(id=pk)
        registro.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def unidades_list(request):
    if request.method == 'GET':
        unidades = Unidad.objects.all()
        serializer = UnidadSerializer(unidades, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UnidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def unidad(request, pk):
    if request.method == 'GET':
        unidad = Unidad.objects.get(id=pk)
        serializer = UnidadSerializer(unidad)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        unidad = Unidad.objects.get(id=pk)
        unidad.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def registros_de_una_estacion(request, estacion_pk):
    try:
        if estacion_pk == 0:
            registros = Registro.objects.all()
        else:
            registros = Registro.objects.filter(estacion=estacion_pk)
        serializer = RegistroSerializer(registros, many=True)
        return Response(serializer.data)
    except Unidad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Registro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def pronosticos_list(request):
    if request.method == 'GET':
        pronosticos = Pronostico.objects.all()
        serializer = PronosticoSerializer(pronosticos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PronosticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#Relacionado con la autenticaci'on

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer