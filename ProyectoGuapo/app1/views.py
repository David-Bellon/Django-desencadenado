from hashlib import new
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
            "pass": password,
            "meta": Usuarios.objects.all()
        }
        if str(user) == "" or str(email) == "" or str(password) == "":
            context["error"] = "Algunos de los campos esta vacio"
            return render(request, "signup.html", context)
        else:
            new_user = Usuarios.objects.create(name= user, password= password, email= email)
            new_user.save()
            return render(request, "signup.html", context)
        
    else:
        context = {
                "meta": Usuarios.objects.all()
            }
        return render(request, "signup.html", context=context)
    

def render_forum(request):
    return render(request, "form.html")
