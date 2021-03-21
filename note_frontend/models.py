from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    thought = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.author.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # profile = models.ImageField(upload_to='users')
    bio = models.TextField(max_length=350)

    def __str__(self):
        return self.user.username