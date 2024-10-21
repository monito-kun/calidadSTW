# eventos/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Documentos,Evento  # Importa tu modelo Documentos

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ['codigo', 'nombre_caso', 'archivo', 'evento']  # Asegúrate de incluir el campo 'evento'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'descripcion', 'tamano', 'duracion', 'tipo_actividades']