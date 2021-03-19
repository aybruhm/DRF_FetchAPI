from django.shortcuts import render
from .serializers import NoteSerializer
from note_frontend.models import Note
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET", "POST"])
def note_list(request):
    """
    This view returns a list of notes.
    """
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    """
    This method creates a new note.
    """
    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def note_detail(request, pk):
    """
    This view returns a single note and also updates.
    """
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(note, many=False)

    """
    This method updates a note
    """
    if request.method == "PUT":
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    This method deletes a note.
    """
    if request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.data)