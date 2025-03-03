# blog/urls.py
from django.urls import path, include
from . import views  # импортируем views из blog
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница приложения blog
    path('api/', include(router.urls)),  # Теперь API доступно по /api/posts/ и /api/comments/
]
