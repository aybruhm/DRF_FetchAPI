from django.urls import path
from .views import note_update, note_delete, note_list, note_overview, note_post, note_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', note_list, name="note-list"),
    path('overview/', note_overview, name="note-overview"),
    path('post/', note_post, name="note-post"),
    path('detail/<int:pk>/', note_detail, name="note-detail"),
    path('update/<int:pk>/', note_update, name="note-update"),
    path('delete/<int:pk>/', note_delete,  name="note-update"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
