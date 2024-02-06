from django.shortcuts import redirect, render

from web.forms import VotacionForm
from .models import EnVivos, Noticia, Regiones, Votaciones
from django.contrib import messages
# Create your views here.
def home(request):
    first_noticia = Noticia.objects.last()
    old_noticia = Noticia.objects.all().order_by('-id')[1:5]
    info_regiones = Regiones.objects.all()[0:15]
    info_region_magallanes = Regiones.objects.filter(id=16)
    en_vivo = EnVivos.objects.first()
    resultados_votos = Regiones.objects.all().order_by('-votos')[0:3]
    if request.method == 'POST':
        form = VotacionForm(request.POST)
        if form.is_valid():
            region_id = form.cleaned_data['region_id']
            region_nombre = Regiones.objects.get(pk=region_id).nombreRegion
            region = Regiones.objects.get(pk=region_id)
            user_ip = request.META.get('REMOTE_ADDR')

            # Verifica si la IP ya ha votado
            #if Votaciones.objects.filter(ip=user_ip).exists():
                #messages.warning(request, "Ya has votado por una región.")

            #else:
            region.votos += 1
            region.save()
            Votaciones.objects.create(ip=user_ip, nombreRegion=region)
            messages.success(request, "Tu voto por " + region_nombre + " ha sido añadido correctamente.")
            return redirect('home') 
    else:
        form = VotacionForm()
    return render(request, 'web/index.html',{
        'first_noticia': first_noticia,
        'old_noticia': old_noticia,
        'info_regiones': info_regiones,
        'info_region_magallanes': info_region_magallanes,
        'en_vivo': en_vivo,
        'form': form,
        'resultados_votos': resultados_votos
    })