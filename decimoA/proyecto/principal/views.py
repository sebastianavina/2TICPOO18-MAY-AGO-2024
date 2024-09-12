from django.shortcuts import render

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "principal/index.html", {})


def manifest(request):
    return render(request, "principal/manifest.json", {})
