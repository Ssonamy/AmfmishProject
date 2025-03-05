from django.contrib import admin
from django.urls import path, include
from blog.views import index


urlpatterns = [
    path('', index, name='home'),  # Теперь главная страница работает!
    path('admin/', admin.site.urls),  # Админка
    path('blog/', include('blog.urls')),  # Маршруты из приложения blog
    path('users/', include('users.urls')),  # Маршруты из приложения users
]
