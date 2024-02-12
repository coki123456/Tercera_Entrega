from django import forms

class FormularioCreacionPost(forms.Form):
    titulo = forms.CharField(max_length=20)
    autor = forms.CharField(max_length=30)
    texto = forms.CharField()
    fecha_post = forms.DateTimeField()