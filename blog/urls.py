from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import index

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='index'),
]

