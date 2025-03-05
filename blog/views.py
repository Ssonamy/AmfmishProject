from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import UploadedImage
from .models import Post

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('blog:upload_image')
    else:
        form = ImageUploadForm()

    images = UploadedImage.objects.filter(user=request.user)
    return render(request, 'blog/upload.html', {'form': form, 'images': images})
=======

>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
def index(request):
    return HttpResponse("Главная страница блога!")

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
<<<<<<< HEAD

def index(request):
    posts = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/index.html', {'posts': posts})
=======
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
