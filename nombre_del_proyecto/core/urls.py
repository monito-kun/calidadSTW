from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', home, name='index'),
    path('login/', views.user_login, name='login'),  # Actualizar referencia a user_login
    path('logout/', views.user_logout, name='logout'),  # Añadir ruta para logout
    path('eventos/', views.eventos, name='eventos'),
    path('listaong/', views.listaong, name='listaong'),
    path('cetificado/', views.certificado, name='certificado'),
    path('registro/', views.registro, name='registro'),
    path('userIndex/', views.userIndex, name='userIndex'),
    path('lodinAdmin/', views.loginAdmin, name='loginAdmin'),
    path('indexAdmin/', views.indexAdmin, name='indexAdmin'),
    path('generarReporte/', views.generarReporte, name='generarReporte'),  # Actualizar referencia a generarReporte
    path('generarReporte/', views.generarReporte, name='generarReporte'),  # Ruta para subir documentos sin evento_id
    path('generarReporte/<int:evento_id>/', views.generarReporte, name='generarReporte'),  # Ruta para generar reporte con evento_id
]
