from django.db import models
from django.contrib import admin

# Create your models here.

class Usuarios(models.Model):
    followers = models.IntegerField(null=False)
    total_likes = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    image = models.ImageField(null=True, upload_to= "profile")

class Tweets(models.Model):
    text = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)


admin.site.register(Usuarios)
admin.site.register(Tweets)