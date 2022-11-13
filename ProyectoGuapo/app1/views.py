from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Tweets, Usuarios
from django.contrib.auth.hashers import make_password
from pathlib import Path
from django.core.files import File
import json
from cryptography.fernet import Fernet
import base64
# Create your views here.

Key = b'qRn_b51FoQ_kskeHxfQxnKhM3X98Z-jXx7wGRTXhyNw='
oscar = Fernet(Key)

def index(request):
    
    context = {}
    if request.COOKIES.get("id") is None:
        context = {
            "profile_picture": "static\images\generic.svg",
            "loged": False
        }
    else:
        #if cookie exists take the user name, followers, total likes
        #Look in the data base the profile picture and put in context
        
        cookie = oscar.decrypt(request.COOKIES.get("id").encode('utf-8')).decode()

        user = Usuarios.objects.filter(id = cookie)
        user_image = str(user[0].image)
        if user_image == "":
            user_image = "static/images/generic.svg"
        else:
            user_image = "media/" + user_image
        context = {
            "profile_picture": user_image,
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
        try:
            image = request.FILES["imagefield"]
        except:
            image = None
        context = {}

        if str(user) == "" or str(email) == "" or str(password) == "":
            context["error"] = "Algunos de los campos esta vacio"
            return render(request, "signup.html", context)
        else:
            password = make_password(password)
            new_user = Usuarios.objects.create(name= user, password= password, email= email, followers = 0, total_likes = 0, image=image)
            new_user.save()
            #response = render(request, 'index.html')
            response = HttpResponseRedirect("/")
            response.set_cookie('id', oscar.encrypt(str(new_user.id).encode()).decode(), max_age=60000)
            return response
        
    else:
        context = {
                "meta": Usuarios.objects.all()
            }
        return render(request, "signup.html", context=context)

def profile(request, profile_name):
    context = {
        "user_name": profile_name
    }
    return render(request, "profile.html", context=context)

def tweet(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("UTF-8"))
        cookie = request.COOKIES.get("id")
        user = Usuarios.objects.filter(id = cookie)[0]
        text = data["text"]
        new_tweet = Tweets.objects.create(text= text, user=user)
        new_tweet.save()
        response = HttpResponseRedirect("/")
        return response
