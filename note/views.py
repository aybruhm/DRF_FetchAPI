from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer

# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def note_list(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)
