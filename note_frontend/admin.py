from django.contrib import admin
from .models import Note, Profile


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio')


admin.site.register(Note, NoteAdmin)
admin.site.register(Profile, ProfileAdmin)