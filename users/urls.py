from django.urls import path
<<<<<<< HEAD
from .views import users_list, user_profile, upload_image
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('<int:user_id>/', user_profile, name='user_profile'),
    path('', users_list, name='users_list'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # path('upload/', views.upload_image, name='upload'),
=======
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),  # Главная страница пользователей
>>>>>>> a5b6113 (Добавил рестфреймворк а также круд операции)
]
