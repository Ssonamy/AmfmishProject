from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from home.views import home  # Меняем импорт: теперь главная страница берётся из home/views.py

urlpatterns = [
    path('', home, name='home'),  # Главная страница теперь из home/views.py
=======
from blog.views import index


urlpatterns = [
    path('', index, name='home'),  # Теперь главная страница работает!
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
    path('admin/', admin.site.urls),  # Админка
    path('blog/', include('blog.urls')),  # Маршруты из приложения blog
    path('users/', include('users.urls')),  # Маршруты из приложения users
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)