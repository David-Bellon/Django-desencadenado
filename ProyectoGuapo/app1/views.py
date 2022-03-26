from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Usuarios
from django.contrib.auth.hashers import make_password
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
        cookie = request.COOKIES.get("name")
        user = Usuarios.objects.filter(name = cookie)
        context = {
            "profie-picture": "path to the picture in the db",
            "loged": True,
            "user_name": user[0].name,
            "followers": user[0].followers,
            "total_likes": user[0].total_likes,
            "cookie": cookie
        }

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
            password = make_password(password)
            new_user = Usuarios.objects.create(name= user, password= password, email= email, followers = 0, total_likes = 0)
            new_user.save()
            #response = render(request, 'index.html')
            response = HttpResponseRedirect("/")
            response.set_cookie('name', str(user), max_age=60000)
            return response
        
    else:
        context = {
                "meta": Usuarios.objects.all()
            }
        return render(request, "signup.html", context=context)

def profile(request):
    return render(request, "profile.html")
