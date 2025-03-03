from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()  # Содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f'Комментарий к "{self.post.title}"'
