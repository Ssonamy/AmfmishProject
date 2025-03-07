from django.urls import path
from .views import users_list, user_profile

urlpatterns = [
    path('<int:user_id>/', user_profile, name='user_profile'),
    path('', users_list, name='users_list'),
]
