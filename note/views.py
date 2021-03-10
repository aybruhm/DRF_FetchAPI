from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer

# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

@api_view(["GET"])
def note_overview(request, format=None):
    note_urls = {
        'Get Notes': 'note/',
        'Create Note': 'note/post/',
        'Detail Note': 'note/<int:pk>/',
        'Update Note': 'note/update/<int:pk>/',
        'Delete Note': 'note/delete/<int:pk>/',
    }
    return Response(note_urls)


@api_view(["GET"])
def note_list(request, format=None):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def note_detail(request, pk, format=None):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def note_post(request, format=None):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def note_update(request, pk, format=None):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def note_delete(request, pk, format=None):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Note.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)
