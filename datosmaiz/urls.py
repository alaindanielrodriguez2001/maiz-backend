from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Rutas para la API
urlpatterns = [   
    path('estaciones/', views.estaciones_list, name='estaciones'),
    path('estacion/<int:pk>', views.estacion, name='estacion'),
    
    path('registros/', views.registros_list, name='registros'),
    path('registro/<int:pk>', views.registro, name='registro'),
    path('registros_estacion/<int:pk>', views.registros_de_una_estacion, name='registros_estacion'),

    
    path('unidades/', views.unidades_list, name='unidades'),
    path('unidad/<int:pk>', views.unidad, name='unidad'),
    
    path('pronosticos/', views.pronosticos_list, name='pronosticos'),
    path('pronostico/<int:pk>', views.pronostico, name='pronostico'),
    
    
    #Relacionado con la autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    
    
    
    
    #Para añadir instancias de prueba
    path('add_registros/', views.add_registros)
]