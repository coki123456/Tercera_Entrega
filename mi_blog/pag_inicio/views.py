from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pag_principal(request):
    return render(request, 'pag_principal.html')

def usuario(request):
    return render(request, 'usuarios.html')