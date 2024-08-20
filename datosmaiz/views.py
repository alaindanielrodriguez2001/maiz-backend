from .models import Campo, Observacion
from .serializers import CampoSerializer, ObservacionSerializer, RegisterSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAuthenticatedOrReadOnly


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def observaciones_list(request):
    """
    Lista de las observaciones.
    """
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
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def campos_list(request):
    """
    Lista de los campos.
    """

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
    

@api_view(['GET'])
@permission_classes([AllowAny])
def observaciones_de_un_campo(request, campo_pk):
    """
    Lista de las observaciones de un campo en específico.
    """
    try:
        print(f"Cargando las observaciones del campo: {campo_pk}")
        if campo_pk == 0:
            observaciones = Observacion.objects.all()
        else:
            observaciones = Observacion.objects.filter(campo_id=campo_pk)
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)
    except Campo.DoesNotExist:
        print(f"El campo {campo_pk} no existe.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Observacion.DoesNotExist:
        print(f"No se encontraron observaciones para el campo {campo_pk}.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer