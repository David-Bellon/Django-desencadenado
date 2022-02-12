from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == "POST":
        data = request.POST.get("textfield", None)
        context = {
            "texto": data
        }
        return render(request, "hola.html", context)
    else:
        return render(request, 'hola.html')

def nada(request):
    return render(request, "pruebas.html")
