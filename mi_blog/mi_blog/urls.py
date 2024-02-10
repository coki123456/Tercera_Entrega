
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('pag_inicio.urls')),
    path('usuarios/', include('usuarios.urls'))
]