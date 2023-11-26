from django.db import models
from users.models import  User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1024)
    title = models.CharField(max_length=128)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)