from django.urls import path
from .views import note_list, note_post, note_update

urlpatterns = [
    path('', note_list, name="note-list"),
    path('post/', note_post, name="note-post"),
    path('update/<int:pk>/', note_update, name="note-update"),
]
