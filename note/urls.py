from django.urls import path
from .views import note_list, note_post

urlpatterns = [
    path('', note_list, name="note-list"),
    path('post/', note_post, name="note-post"),
]
