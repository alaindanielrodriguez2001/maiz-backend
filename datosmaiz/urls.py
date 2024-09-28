from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Rutas para la API
urlpatterns = [   
    path('estaciones/', views.estaciones_list),
    path('estacion/<int:pk>', views.estacion),
    
    path('registros/', views.registros_list),
    path('registro/<int:pk>', views.registro),
    path('registros_estacion/<int:pk>', views.registros_de_una_estacion),

    
    path('unidades/', views.unidades_list),
    path('unidad/<int:pk>', views.unidad),
    
    path('pronosticos/', views.pronosticos_list),
    path('pronostico/<int:pk>', views.pronostico),
    
    
    #Relacionado con la autenticación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
]