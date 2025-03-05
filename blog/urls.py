from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from .views import PostViewSet, index, upload_image

app_name = 'blog'  # <--- Добавляем пространство имен
=======
from .views import PostViewSet
from .views import index
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
<<<<<<< HEAD
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
]

urlpatterns += [
    path('upload/', upload_image, name='upload_image'),
]
=======
    path('', index, name='index'),
]

>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
