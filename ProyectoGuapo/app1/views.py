from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios
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
    if request.method == "POST":
        user = request.POST.get("textfield")
        email = request.POST.get("emailfield")
        password = request.POST.get("passwordfield")
        
        context = {
            "name": user,
            "email": email,
            "pass": password
        }
        if str(user) == "" or str(email) == "" or str(password) == "":
            context = {"error": "Algunos de los campos esta vacio"}
            return render(request, "pruebas.html", context)
        else:
            Usuarios.objects.create(name= user, password= password)
            return render(request, "pruebas.html", context)
        
    else:
        return render(request, "pruebas.html")
    

def render_forum(request):
    return render(request, "form.html")
