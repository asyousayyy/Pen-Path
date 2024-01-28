from django.db import models
from django.contrib.auth import get_user_model

#post
#title, content, author, updated_at, created_at

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
