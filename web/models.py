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