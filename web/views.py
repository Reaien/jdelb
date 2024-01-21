from django.shortcuts import render
from .models import Noticia
# Create your views here.
def home(request):
    first_noticia = Noticia.objects.last()
    old_noticia = Noticia.objects.all().order_by('-id')[1:5]
    return render(request, 'web/index.html',{
        'first_noticia': first_noticia,
        'old_noticia': old_noticia
    })