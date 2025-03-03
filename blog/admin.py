from django.contrib import admin
from users.models import UserProfile
from .models import Post, Comment

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
