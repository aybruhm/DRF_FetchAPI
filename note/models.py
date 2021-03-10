from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    thought = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ''

    def __str__(self):
        return self.author.username
