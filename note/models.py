from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    thought = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
