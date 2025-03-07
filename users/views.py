from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post  # Импортируем модель постов

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Получаем пользователя
    posts = Post.objects.filter(author=user)  # Получаем его посты
    return render(request, 'users/profile.html', {'user': user, 'posts': posts})

def users_list(request):
    users = User.objects.all()  # Получаем всех пользователей
    return render(request, 'users/users_list.html', {'users': users})