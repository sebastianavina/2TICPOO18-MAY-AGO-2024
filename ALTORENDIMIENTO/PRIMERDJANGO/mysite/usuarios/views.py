from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#from models import Usuario, Materia


def index(request):


    respuesta = "aqui son los agregados"

    usuarios = Usuario.objects.all()

    for u in usuarios:
        respuesta += u.usuario + "<br />"
    
    return HttpResponse(respuesta)



def alumno(request, alumno):

    if "agregar" in request.GET:
        nuevo_usuario = Usuario()
        nuevo_usuario.usuario = alumno
        nuevo_usuario.save()
        
    
    respuesta = """

    Esta es la pagina de """+alumno+"""

    <form method="GET" action=".">
    <input type="submit" name="agregar" />
    </form>
    
    
    """

    return HttpResponse(respuesta)
