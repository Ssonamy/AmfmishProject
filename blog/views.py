from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    return HttpResponse("Главная страница блога!")

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/index.html', {'posts': posts})
