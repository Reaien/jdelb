from django import forms
from .models import Noticia

class VotacionForm(forms.Form):
    region_id = forms.IntegerField(widget=forms.HiddenInput())

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'textoNoticia1', 'textoNoticia2', 'imagenEncabezado', 'imagenPrincipal', 'imagenSecundaria']