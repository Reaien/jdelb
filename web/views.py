from django.shortcuts import redirect, render
from django.http import JsonResponse
from web.forms import VotacionForm, NoticiaForm
from .models import EnVivos, Noticia, Regiones, Votaciones, Campeones, BloqueVotaciones, Comuna, Region, Inscripcion
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import permission_required
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
    if request.method == "POST" and 'region_id' in request.method == 'POST':
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
    elif request.method == "POST" and 'enviar_inscripcion' in request.POST:  # Identifica el formulario de inscripción
        # Recoge los datos del formulario de inscripción
        
        region_id = request.POST.get('region_inscripcion')
        comuna_id = request.POST.get('comuna_inscripcion')
        nombre_bailarina = request.POST.get('nombre_bailarina')
        edad_bailarina = request.POST.get('edad_bailarina')
        fecha_nacimiento_bailarina = request.POST.get('fecha_nacimiento_bailarina')
        rut_bailarina = request.POST.get('rut_bailarina')
        email_bailarina = request.POST.get('email_bailarina')
        telefono_bailarina = request.POST.get('fono_bailarina')
        nombre_bailarin = request.POST.get('nombre_bailarin')
        edad_bailarin = request.POST.get('edad_bailarin')
        fecha_nacimiento_bailarin = request.POST.get('fecha_nacimiento_bailarin')
        rut_bailarin = request.POST.get('rut_bailarin')
        email_bailarin = request.POST.get('email_bailarin')
        telefono_bailarin = request.POST.get('fono_bailarin')
        print(request.POST)
        region = Region.objects.get(id=region_id)
        comuna = Comuna.objects.get(id=comuna_id)

        #obtener el correo por id de región seleccionada
        if region.id == 1:
            mail_destino = 'arica@jdelb.cl'
        elif region.id == 2:
            mail_destino = 'tarapaca@jdelb.cl'
        elif region.id == 3:
            mail_destino = 'antofagasta@jdelb.cl'
        elif region.id == 4:
            mail_destino = 'atacama@jdelb.cl'
        elif region.id == 5:
            mail_destino = 'coquimbo@jdelb.cl'
        elif region.id == 6:
            mail_destino = 'valparaiso@jdelb.cl'
        elif region.id == 7:
            mail_destino = 'metropolitana@jdelb.cl'
        elif region.id == 8:
            mail_destino = 'ohiggins@jdelb.cl'
        elif region.id == 9:
            mail_destino = 'delmaule@jdelb.cl'
        elif region.id == 10:
            mail_destino = 'nuble@jdelb.cl'
        elif region.id == 11:
            mail_destino = 'biobio@jdelb.cl'
        elif region.id == 12:
            mail_destino = 'araucania@jdelb.cl'
        elif region.id == 13:
            mail_destino = 'losrios@jdelb.cl'
        elif region.id == 14:
            mail_destino = 'loslagos@jdelb.cl'
        elif region.id == 15:
            mail_destino = 'aysen@jdelb.cl'
        elif region.id == 16:
            mail_destino = 'magallanes@jdelb.cl'
        else:
            return
        
        

        # Guardar los datos en la base de datos
        inscripcion = Inscripcion.objects.create(
            #datos bailarina form
            region=region.nombre,
            comuna=comuna.nombre,
            nombre_bailarina=nombre_bailarina,
            edad_bailarina=edad_bailarina,
            fecha_nacimiento_bailarina=fecha_nacimiento_bailarina,
            rut_bailarina=rut_bailarina,
            email_bailarina=email_bailarina,
            telefono_bailarina=telefono_bailarina,
            #datos bailarin form
            nombre_bailarin=nombre_bailarin,
            edad_bailarin=edad_bailarin,
            fecha_nacimiento_bailarin=fecha_nacimiento_bailarin,
            rut_bailarin = rut_bailarin,
            email_bailarin=email_bailarin,
            telefono_bailarin=telefono_bailarin

        )
        messages.success(request, "Tu inscripción ha sido enviada correctamente.") 
        inscripcion.save()
                # Enviar correo electrónico
        subject = "Nueva inscripción recibida"
        message = f"""
        Nueva inscripción recibida:

        Región: {region}
        Comuna: {comuna}
        
        Datos de la Bailarina:
        Nombre: {nombre_bailarina}
        Edad: {edad_bailarina}
        Fecha de Nacimiento: {fecha_nacimiento_bailarina}
        RUT: {rut_bailarina}
        Email: {email_bailarina}
        Teléfono: {telefono_bailarina}

        Datos del Bailarín:
        Nombre: {nombre_bailarin}
        Edad: {edad_bailarin}
        Fecha de Nacimiento: {fecha_nacimiento_bailarin}
        RUT: {rut_bailarin}
        Email: {email_bailarin}
        Teléfono: {telefono_bailarin}
        """

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [mail_destino, 'director@jdelb.cl'],
            fail_silently=False
        )
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

@permission_required('web.add_noticia')
def crearNoticia(request):
    data = {
        'form': NoticiaForm()
    }

    if request.method == "POST":
        form = NoticiaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request, "Noticia creada correctamente.") 
            form.save()
        else:
            data['form'] = form


    return render(request, 'web/crearNoticia.html', data)

def noticia(request, id):
    listaNoticias = Noticia.objects.all()
    noticia = Noticia.objects.get(id = id)
    data = {"noticia" : noticia,
            "listaNoticias" : listaNoticias}
    return render(request, 'web/noticia.html', data)