from django.db import models


# Create your models here.
class Posteo(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    texto = models.TextField(max_length=500)
    fecha_post = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo