from django.db import models

# Create your models here.

class Usuarios(models.Model):
    followers = models.IntegerField(null=False)
    total_likes = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    def getFollowers(self):
        return self.followers

    def getTotalLikes(self):
        return self.total_likes
