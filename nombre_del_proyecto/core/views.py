from django.shortcuts import render
def home(request):
    return render(request, 'core/index.html')
def login(request):
    return render(request, 'core/login.html')
def eventos(request):
    return render(request, 'core/eventos.html')
def listaong(request):
    return render(request, 'core/listaong.html')
def certificado(request):
    return render(request, 'core/certificado.html')
def registro(request):  
    return render(request, 'core/registro.html')
def userIndex(request):  
    return render(request, 'core/userIndex.html')
def loginAdmin(request):  
    return render(request, 'core/loginAdmin.html')
def indexAdmin(request):  
    return render(request, 'core/indexAdmin.html')

# Create your views here.
