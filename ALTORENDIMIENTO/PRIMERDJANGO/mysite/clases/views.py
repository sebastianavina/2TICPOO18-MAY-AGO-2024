from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index(request):

    casilla3 = "."
    
    if "casilla" in request.GET:
        if int(request.GET["casilla"]) == 3:
            casilla3 = "x"
    

    respuesta = """
<html>
    <body>
    <table border="1">
    <tr>
    <td><a href="/feliz?casilla=1">.</a></td>
    <td><a href="/feliz?casilla=2">.</a></td>
    <td><a href="/feliz?casilla=3">"""+casilla3+"""</a></td>
    </tr>
    <tr>
    <td><a href="/feliz?casilla=4">.</a></td>
    <td><a href="/feliz?casilla=5">.</a></td>
    <td><a href="/feliz?casilla=6">.</a></td>
    </tr>
    <tr>
    <td><a href="/feliz?casilla=7">.</a></td>
    <td><a href="/feliz?casilla=8">.</a></td>
    <td><a href="/feliz?casilla=9">.</a></td>
    </tr>
    </table>
    </body>
</html>
    """

    
    return HttpResponse(respuesta)
