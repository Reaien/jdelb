from django import forms
from .models import Regiones

class VotacionForm(forms.Form):
    region_id = forms.IntegerField(widget=forms.HiddenInput())