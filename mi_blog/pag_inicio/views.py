from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posteo
from .forms import FormularioCreacionPost

# Create your views here.
def pag_principal(request):
    return render(request, 'pag_principal.html')

def posteos(request):
    post = Posteo.objects.all()
    return render(request, 'posteos.html', {'posteos': post})

def crear_posteo(request):
    formulario = FormularioCreacionPost()
    if request.method == "POST":
        formulario = FormularioCreacionPost(request.POST)
        if formulario.is_valid():
            titulo = formulario.cleaned_data.get('titulo')
            autor = formulario.cleaned_data.get('autor')
            texto = formulario.cleaned_data.get('texto')
            post = Posteo(titulo=titulo, autor=autor, texto=texto)
            post.save()
            return redirect("posteos")
        
    return render(request, 'crear_posteo.html', {'formulario': formulario})