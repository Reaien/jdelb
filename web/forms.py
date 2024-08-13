from django import forms
from .models import Noticia

class VotacionForm(forms.Form):
    region_id = forms.IntegerField(widget=forms.HiddenInput())

class NoticiaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"style":"height: 150px"}))
    textoNoticia1 = forms.CharField(widget=forms.Textarea(attrs={"style":"height: 200px"}))
    textoNoticia2 = forms.CharField(widget=forms.Textarea(attrs={"style":"height: 200px"}))
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'textoNoticia1', 'textoNoticia2', 'imagenPreview', 'imagenPrincipal', 'imagenSecundaria']