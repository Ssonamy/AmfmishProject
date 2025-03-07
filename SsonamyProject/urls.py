from django.contrib import admin
from django.urls import path, include
from home.views import home  # Меняем импорт: теперь главная страница берётся из home/views.py

urlpatterns = [
    path('', home, name='home'),  # Главная страница теперь из home/views.py
    path('admin/', admin.site.urls),  # Админка
    path('blog/', include('blog.urls')),  # Маршруты из приложения blog
    path('users/', include('users.urls')),  # Маршруты из приложения users
]
