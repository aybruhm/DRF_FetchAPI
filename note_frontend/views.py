from django.shortcuts import render


def home(request):
    return render(request, "note_frontend/home.html")


def create_thought(request):
    return render(request, "note_frontend/write-thought.html")


def update_thought(request):
    return render(request, "note_frontend/edit-thought.html")


def delete_thought(request):
    return render(request, "note_frontend/confirm-delete.html")


def login(request):
    return render(request, "note_frontend/login.html")


def register(request):
    return render(request, "note_frontend/register.html")


def profile(request):
    return render(request, "note_frontend/profile.html")
