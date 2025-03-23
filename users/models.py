from django.db import models
from django.contrib.auth.models import User
import os
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Профиль {self.user.username}'

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('image', filename)

class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=user_directory_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)