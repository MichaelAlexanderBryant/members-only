from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    member = models.BooleanField(null=True, blank=True, default=False)
