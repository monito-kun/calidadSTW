
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='index'),
    path('login/', login, name='login'),
    path('eventos/', eventos, name='eventos'),
     path('listaong/', listaong, name='listaong'),
     path('cetificado/', certificado, name='certificado'),
     path('registro/', registro, name='registro'),
     path('userIndex/', userIndex, name='userIndex'),
     path('lodinAdmin/', loginAdmin, name='loginAdmin'),
     path('indexAdmin/', indexAdmin, name='indexAdmin'),
]
