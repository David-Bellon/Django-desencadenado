from django.db import models

# Create your models here.

class Usuarios(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True)
    followers = models.IntegerField(null=False)
    total_likes = models.IntegerField(null=False)
    name = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)


    def getUser(self):
        return self.user_id

    def getFollowers(self):
        return self.followers

    def getTotalLikes(self):
        return self.total_likes
