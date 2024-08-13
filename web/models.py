from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=30, null=True)
    fecha = models.DateField(auto_now_add=True, null=True)
    descripcion = models.CharField(max_length=250, null=True)
    textoNoticia1 = models.CharField(max_length=1250, null=True)
    textoNoticia2 = models.CharField(max_length=1450, null=True, blank=True)
    imagenPreview = models.ImageField(upload_to="images", null=True, blank=True)
    imagenPrincipal = models.ImageField(upload_to="images", null=True, blank=True)
    imagenSecundaria = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        db_table = 'Noticia'

    def __str__(self):
        return self.titulo  
    
class Regiones(models.Model):
    nombreRegion = models.CharField(max_length=50, null=True)
    nombreCompletoDelegado = models.CharField(max_length=100, null=True)
    correoDelegado = models.CharField(max_length=150, null=True, blank=True)
    fotoDelegado = models.ImageField(upload_to="images", null=True, blank=True)
    nombreCompletoCompetidor = models.CharField(max_length=100, null=True, blank=True, default="")
    fotoCompetidor = models.ImageField(upload_to="images", null=True, blank=True)
    nombreCompletoCompetidora = models.CharField(max_length=100, null=True, blank=True, default="")
    fotoCompetidora = models.ImageField(upload_to="images", null=True, blank=True)
    imagenRegion = models.ImageField(upload_to="images", null=True)
    votos = models.IntegerField(default=0)

    class Meta:
        db_table = 'Regiones'

    def __str__(self):
        return self.nombreRegion
    
class Votaciones(models.Model):
    ip = models.GenericIPAddressField()
    nombreRegion = models.ForeignKey(Regiones, on_delete=models.PROTECT)

    class Meta:
        db_table = 'Votacion'
    
class EnVivos(models.Model):
    activar_en_vivo = models.BooleanField( default=False)
    link_transmision = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'EnVivos'

    def __str__(param):
        param = 'Activar Bloque en vivo'
        return param
    
class BloqueVotaciones(models.Model):
    activar_votaciones = models.BooleanField(default=False)
    class Meta:
        db_table = 'Votaciones'
    def __str__(param):
        param = 'Activar bloque votaciones'
        return param
    
class Campeones(models.Model):
    nombre_pareja = models.CharField(max_length=100, null=True)
    anno_campeon = models.CharField(max_length=5, null=True)
    foto_campeones = models.ImageField(upload_to="images", null=True)

    class Meta:
        db_table = 'Campeones'

    def __str__(self):
        return self.anno_campeon
    
class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Inscripcion(models.Model):
    region = models.CharField(max_length=100)  # Ahora almacena el nombre en lugar del ID
    comuna = models.CharField(max_length=100)  # Ahora almacena el nombre en lugar del ID
    nombre_bailarina = models.CharField(max_length=100)
    edad_bailarina = models.PositiveIntegerField()
    fecha_nacimiento_bailarina = models.DateField()
    rut_bailarina = models.CharField(max_length=12)
    email_bailarina = models.EmailField()
    telefono_bailarina = models.CharField(max_length=15)
    nombre_bailarin = models.CharField(max_length=100)
    edad_bailarin = models.PositiveIntegerField()
    fecha_nacimiento_bailarin = models.DateField()
    rut_bailarin = models.CharField(max_length=12)
    email_bailarin = models.EmailField()
    telefono_bailarin = models.CharField(max_length=15)

    def __str__(self):
        return f"Inscripción de {self.nombre_bailarina} y {self.nombre_bailarin}"