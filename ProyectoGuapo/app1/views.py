from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Usuarios
# Create your views here.

def index(request):
    context = {}
    if request.COOKIES.get("name") is None:
        context = {
            "picture": "static\images\profie-none.svg",
            "loged": False
        }
    else:
        #if cookie exists take the user name, followers, total likes
        #Look in the data base the profile picture and put in context
        #context = {
        #    "profie-picture": "path to the picture in the db"
        #    "loged": True
        #    "user_name": -----
        #    "followers": -----
        #    "total_ikes": -----
        #}
        None

    return render(request, 'index.html', context=context)

def sign_up(request):
    if request.method == "POST":
        user = request.POST.get("textfield")
        email = request.POST.get("emailfield")
        password = request.POST.get("passwordfield")

        context = {}

        if str(user) == "" or str(email) == "" or str(password) == "":
            context["error"] = "Algunos de los campos esta vacio"
            return render(request, "signup.html", context)
        else:
            new_user = Usuarios.objects.create(name= user, password= password, email= email)
            new_user.save()
            #response = render(request, 'index.html')
            response = HttpResponseRedirect("/")
            response.set_cookie('name', str(user), max_age=600)
            return response
        
    else:
        context = {
                "meta": Usuarios.objects.all()
            }
        return render(request, "signup.html", context=context)
