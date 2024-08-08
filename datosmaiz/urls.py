from django.urls import path
from . import views

urlpatterns = [
    path('observaciones/', views.observaciones_list),
    path('observaciones/<int:pk>/', views.observacion_detail),
    path('campos/', views.campos_list),
    path('campos/<int:pk>/', views.campo_detail),
]