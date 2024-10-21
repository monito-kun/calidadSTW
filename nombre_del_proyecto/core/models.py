from django.db import models
from django.contrib.auth.models import User



class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True, null=True)
    tamano = models.IntegerField(help_text="Número de asistentes")
    duracion = models.FloatField(help_text="Duración del evento en horas")
    tipo_actividades = models.CharField(max_length=250, help_text="Descripción de las actividades")

    def __str__(self):
        return self.nombre

class Documentos(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre_caso = models.CharField(max_length=250)
    archivo = models.FileField(upload_to='documentos/')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)  # Asegúrate de que este campo esté definido

    def __str__(self):
        return f"{self.nombre_caso} ({self.codigo}) ({self.archivo.name})"

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    # Puedes añadir más campos si es necesario
    def __str__(self):
        return self.user.username
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade campos adicionales aquí si es necesario
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username

