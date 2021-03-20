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
    print(request.user)

    if request.method == "POST":
        
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            thought = form.cleaned_data["thought"]
            note = Note(
                title=title,
                thought=thought,
                author=request.user,
            )
            note.save()
            return redirect("note:home")
        return redirect("note:new-thought")

    context = {
        'form': form
    }
    return render(request, "note_frontend/write-thought.html", context)


def update_thought(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return redirect("note:home")

    # TODO:
    # - import update_thought form
    # - implement updat/post method
    # - uhh?
    return render(request, "note_frontend/edit-thought.html")


def delete_thought(request, pk):
    return render(request, "note_frontend/confirm-delete.html")


def login(request):
    return render(request, "note_frontend/login.html")


def register(request):
    return render(request, "note_frontend/register.html")


def profile(request):
    return render(request, "note_frontend/profile.html")
