from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User
from account.models import CustomUser
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


def __str__(self):
    return self.title