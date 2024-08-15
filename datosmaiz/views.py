from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Campo, Observacion
from .serializers import CampoSerializer, ObservacionSerializer


@api_view(['GET', 'POST'])
def observaciones_list(request):
    """
    Lista de las observaciones.
    """

    if request.method == 'GET':
        observaciones = Observacion.objects.all()
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ObservacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def observacion_detail(request, pk):
    """
    Lee, actualiza o elimina una observacion.
    """
    try:
        observacion = Observacion.objects.get(pk=pk)
    except Observacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObservacionSerializer(observacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ObservacionSerializer(observacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        observacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def last_observaciones_list(request):
    if request.method == 'GET':
        observaciones = Observacion.objects.all().order_by('-fecha')[:10]
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ObservacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
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
    

@api_view(['GET', 'PUT', 'DELETE'])
def campo_detail(request, pk):
    """
    Lee, actualiza o elimina un campo.
    """
    try:
        campo = Campo.objects.get(pk=pk)
    except Campo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CampoSerializer(campo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CampoSerializer(campo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        campo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def observaciones_de_un_campo(request, campo_pk):
    """
    Lista de las observaciones de un campo en específico.
    """
    try:
        print(f"Fetching observations for campo ID: {campo_pk}")
        if campo_pk == 0:
            observaciones = Observacion.objects.all()
        else:
            observaciones = Observacion.objects.filter(campo_id=campo_pk)
        serializer = ObservacionSerializer(observaciones, many=True)
        return Response(serializer.data)
    except Campo.DoesNotExist:
        print(f"Campo with ID {campo_pk} does not exist.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Observacion.DoesNotExist:
        print(f"No observations found for campo ID {campo_pk}.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"An error occurred: {e}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)