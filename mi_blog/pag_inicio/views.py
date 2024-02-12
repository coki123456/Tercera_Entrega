from django.shortcuts import render
from django.http import HttpResponse
from .models import Posteo

# Create your views here.
def pag_principal(request):
    return render(request, 'pag_principal.html')

def posteos(request):
    post = Posteo.objects.all()
    return render(request, 'posteos.html', {'posteos': post})

def crear_posteo(request):
    # if request.method == 'POST':
    #     autor = request.POST['autor']
    #     titulo = request.POST['titulo']
    #     texto = request.POST['texto']
    #     posteo = Posteo(autor=autor, titulo=titulo, texto=texto)
    #     posteo.save()
    #     return render(request, 'posteos.html', {'posteos': post})
    # else:
    return render(request, 'crear_posteo.html')