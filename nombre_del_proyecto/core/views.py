from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm, DocumentForm, EventoForm
from .models import Evento, Documentos


def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

@login_required
def listaong(request):
    eventos = Evento.objects.all()
    return render(request, 'core/listaong.html', {'eventos': eventos})

def certificado(request):
    return render(request, 'core/certificado.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)  # Usar auth_login para evitar conflicto
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def user_logout(request):
    auth_logout(request)
    return redirect('index')

def userIndex(request):
    documentos = Documentos.objects.all()
    return render(request, 'core/userIndex.html', {'Documentos': documentos})

def loginAdmin(request):  
    return render(request, 'core/loginAdmin.html')

def indexAdmin(request):  
    return render(request, 'core/indexAdmin.html')


@login_required
def generarReporte(request, evento_id=None):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_caso = form.save()
            return HttpResponseRedirect('/')  # Redirige a donde quieras después de guardar
    else:
        form = DocumentForm()

    if evento_id:
        # Lógica para manejar la solicitud GET y devolver el documento
        evento = get_object_or_404(Evento, id=evento_id)
        documento = get_object_or_404(Documentos, evento=evento)
        data = {
            'url': documento.archivo.url
        }
        return JsonResponse(data)

    return render(request, 'core/generarReporte.html', {'form': form})

@login_required
def eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar
    else:
        form = EventoForm()
    return render(request, 'core/eventos.html', {'form': form})