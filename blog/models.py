from django.db import models
from django.contrib.auth.models import User  # Подключаем встроенную модель пользователей
<<<<<<< HEAD
import os
import uuid
=======
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

<<<<<<< HEAD
def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"  # Генерируем уникальное имя
    return f'images/user_{instance.user.id}/{unique_filename}'


class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=upload_to)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"

=======
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
