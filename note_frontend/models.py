from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class Note(models.Model):
    title = models.CharField(max_length=100)
    thought = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.author.username

    def get_update_url(self):
        return reverse('note:update-thought', args=[str(self.pk)])

    def get_delete_url(self):
        return reverse('note:delete-thought', args=[str(self.pk)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    profile_picture = models.ImageField(upload_to='users', blank=True, null=True)
    bio = models.TextField(max_length=350)

    """
    TODO:
    - install Pillow
    - uncomment profile column
    - uncomment the pillow import
    """

    def __str__(self):
        return self.user.username

      # Resize User Profile Picture 
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        profile_picture = Image.open(self.profile_picture.path)
        if profile_picture.height > 300 or profile_picture.width > 300:
            output_size = (300, 300)
            profile_picture.thumbnail(output_size)
        print(profile_picture)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
