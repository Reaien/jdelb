from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=30, null=True)
    fecha = models.DateField(auto_now_add=True, null=True)
    descripcion = models.CharField(max_length=250, null=True)
    textoNoticia1 = models.CharField(max_length=450, null=True)
    textoNoticia2 = models.CharField(max_length=450, null=True, blank=True)
    imagenEncabezado = models.ImageField(upload_to="images", null=True, blank=True)
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
    nombreCompletoCompetidor = models.CharField(max_length=100, null=True)
    fotoCompetidor = models.ImageField(upload_to="images", null=True, blank=True)
    nombreCompletoCompetidora = models.CharField(max_length=100, null=True)
    fotoCompetidora = models.ImageField(upload_to="images", null=True, blank=True)
    imagenRegion = models.ImageField(upload_to="images", null=True)

    class Meta:
        db_table = 'Regiones'

    def __str__(self):
        return self.nombreRegion
    
class EnVivos(models.Model):
    activar_en_vivo = models.BooleanField( default=False)

    class Meta:
        db_table = 'EnVivos'
    
