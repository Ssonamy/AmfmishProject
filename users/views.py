<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ImageUploadForm
from blog.models import Post  # Импортируем модель постов

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Получаем пользователя
    posts = Post.objects.filter(author=user)  # Получаем его посты
    return render(request, 'users/profile.html', {'user': user, 'posts': posts})

def users_list(request):
    users = User.objects.all()  # Получаем всех пользователей
    return render(request, 'users/users_list.html', {'users': users})


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('profile')
    else:
        form = ImageUploadForm()
    return render(request, 'users/upload.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались! Теперь войдите в систему.")
            return redirect('login')  # После успешной регистрации перенаправляем на логин
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

=======
from django.http import HttpResponse

def profile(request):
    return HttpResponse("Страница пользователя")
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
