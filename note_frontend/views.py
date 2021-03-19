from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteCreateForm


def home(request):
    notes = Note.objects.all()[:3]
    context = {
        'notes': notes
    }
    return render(request, "note_frontend/home.html", context)


def create_thought(request):
    form = NoteCreateForm()

    if request.method == "POST":
        
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note:home")
        return redirect("note:new-thought")

    context = {
        'form': form
    }
    return render(request, "note_frontend/write-thought.html", context)


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
