from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posting")
    content = models.CharField(max_length=144)
    timestamp = models.DateTimeField()
    likes = models.IntegerField(default=0)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followed")

