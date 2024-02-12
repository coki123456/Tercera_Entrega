from django.contrib import admin
from .models import Posteo

class posteoAdmin(admin.ModelAdmin):
    campo = ('titulo', 'fecha_publicacion', 'texto', 'autor')
    
admin.site.register(Posteo, posteoAdmin)