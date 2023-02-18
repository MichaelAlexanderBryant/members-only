from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user",null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")