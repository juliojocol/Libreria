from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def publicacion_lista(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'pagina/publicacion_lista.html', {'publicaciones':publicaciones})