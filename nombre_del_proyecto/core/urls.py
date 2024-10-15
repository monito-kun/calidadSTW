
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='index'),
    path('login/', login, name='login'),
    path('eventos/', eventos, name='eventos'),
     path('listaong/', listaong, name='listaong'),
     path('cetificado/', certificado, name='certificado'),
]
