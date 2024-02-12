from django.contrib import admin
from .models import posteo

class posteoAdmin(admin.ModelAdmin):
    campo = ('titulo', 'fecha_publicacion', 'texto', 'autor')
    
admin.site.register(posteo, posteoAdmin)