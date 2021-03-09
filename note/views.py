from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer

# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def note_list(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def note_post(request):
    if request.method == "GET":
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
