from django.db import models
from django.utils import timezone

# Create your models here.
class Posteo(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.titulo