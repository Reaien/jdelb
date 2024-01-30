from django.shortcuts import render
from .models import EnVivos, Noticia, Regiones
# Create your views here.
def home(request):
    first_noticia = Noticia.objects.last()
    old_noticia = Noticia.objects.all().order_by('-id')[1:5]
    info_regiones = Regiones.objects.all()[0:15]
    info_region_magallanes = Regiones.objects.filter(id=16)
    en_vivo = EnVivos.objects.first()
    return render(request, 'web/index.html',{
        'first_noticia': first_noticia,
        'old_noticia': old_noticia,
        'info_regiones': info_regiones,
        'info_region_magallanes': info_region_magallanes,
        'en_vivo': en_vivo
    })