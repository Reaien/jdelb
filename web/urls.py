from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crearNoticia', views.crearNoticia, name="crearNoticia"),
    path('noticia/<id>', views.noticia, name="noticia"),
    path('comunas/<int:region_id>/', views.obtener_comunas, name='obtener_comunas'),
]