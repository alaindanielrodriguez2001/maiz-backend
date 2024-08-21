from .models import Campo, Observacion
from .serializers import CampoSerializer, ObservacionSerializer, RegisterSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes

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

    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer