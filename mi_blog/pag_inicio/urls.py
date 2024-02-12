from django.urls import path
from . import views

urlpatterns = [
    path('', views.pag_principal, name='pag_principal'),
    path('posteos/', views.posteos, name='posteos'),
    path('crear_posteo/', views.crear_posteo, name='crear_posteo'),

]
