from django import forms
from datetime import datetime

class FormularioCreacionPost(forms.Form):
    titulo = forms.CharField(max_length=20)
    autor = forms.CharField(max_length=30)
    texto = forms.CharField(widget=forms.Textarea, max_length=500)
    fecha_post = forms.DateTimeField(initial=datetime.now)