from django.shortcuts import redirect, render
from django.http import JsonResponse
from web.forms import VotacionForm
from .models import EnVivos, Noticia, Regiones, Votaciones, Campeones, BloqueVotaciones, Comuna, Region, Inscripcion
from django.contrib import messages
# Create your views here.
def home(request):
    regiones = Region.objects.all()
    first_noticia = Noticia.objects.last()
    old_noticia = Noticia.objects.all().order_by('-id')[1:5]
    info_regiones = Regiones.objects.all()[0:15]
    info_region_magallanes = Regiones.objects.filter(id=16)
    en_vivo = EnVivos.objects.first()
    resultados_votos = Regiones.objects.all().order_by('-votos')[0:3]
    last_campeones = Campeones.objects.last()
    bloque_votacion = BloqueVotaciones.objects.first()
    if request.method == 'POST':
        form = VotacionForm(request.POST)
        if form.is_valid():
            region_id = form.cleaned_data['region_id']
            region_nombre = Regiones.objects.get(pk=region_id).nombreRegion
            region = Regiones.objects.get(pk=region_id)
            user_ip = request.META.get('REMOTE_ADDR')

            # Verifica si el usuario ya ha votado (utilizando una cookie)
            if 'voto_realizado' in request.COOKIES:
                messages.warning(request, "Ya has votado por una región.")
            else:
                region.votos += 1
                region.save()
                Votaciones.objects.create(ip=user_ip, nombreRegion=region)

                # Establece una cookie para rastrear que el usuario ya ha votado
                response = redirect('home')
                response.set_cookie('voto_realizado', 'true', max_age=3600)  # Establece una cookie válida por 1 hora
                messages.success(request, "Tu voto por " + region_nombre + " ha sido añadido correctamente.")
                return response
        elif 'enviar_inscripcion' in request.POST:  # Identifica el formulario de inscripción
            
 # Recoge los datos del formulario de inscripción
            region_id = request.POST.get('region_inscripcion')
            comuna_id = request.POST.get('comuna_inscripcion')
            nombre_bailarina = request.POST.get('nombre')
            edad_bailarina = request.POST.get('edad')
            fechanac_bailarina = request.POST.get('fechanac')
            rut_bailarina = request.POST.get('rut')
            email_bailarina = request.POST.get('email')
            fono_bailarina = request.POST.get('fono')

            # Guardar los datos en la base de datos
            inscripcion = Inscripcion(
                region_id=region_id,
                comuna_id=comuna_id,
                nombre=nombre_bailarina,
                edad=edad_bailarina,
                fecha_nacimiento=fechanac_bailarina,
                rut=rut_bailarina,
                email=email_bailarina,
                telefono=fono_bailarina
            )
            inscripcion.save()
            messages.success(request, "Tu inscripción ha sido enviada correctamente.")
            return redirect('home') 
    else:
        form = VotacionForm()


    # Si la solicitud es AJAX, devuelve los resultados de los votos en formato JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = list(resultados_votos.values('nombreRegion', 'nombreCompletoCompetidora', 'nombreCompletoCompetidor','votos','fotoCompetidora', 'fotoCompetidor'))
        return JsonResponse({'resultados_votos': data})


    return render(request, 'web/index.html',{
        'first_noticia': first_noticia,
        'old_noticia': old_noticia,
        'info_regiones': info_regiones,
        'info_region_magallanes': info_region_magallanes,
        'en_vivo': en_vivo,
        'form': form,
        'resultados_votos': resultados_votos,
        'last_campeones': last_campeones,
        'bloque_votacion' : bloque_votacion,
        'regiones': regiones
        
    })

def obtener_comunas(request, region_id):
    comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)