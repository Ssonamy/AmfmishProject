from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная страница блога!")

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
