from django.shortcuts import render


def home(request):
    return render(request, "note_frontend/index.html")
