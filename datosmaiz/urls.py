from django.urls import path
from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('observaciones/', views.observaciones_list),
    path('observacion/<int:pk>', views.observacion),
    path('observaciones_campo/<int:campo_pk>/', views.observaciones_de_un_campo),
    path('campos/', views.campos_list),
    path('campo/<int:pk>', views.campo),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
]