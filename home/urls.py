from django.urls import path
from .views import home  # Здесь импортируем функцию home из views.py

urlpatterns = [
    path('', home, name='home'),  # Здесь тоже home
]
