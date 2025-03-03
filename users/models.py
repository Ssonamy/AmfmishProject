from django.db import models
from blog.models import Post
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
