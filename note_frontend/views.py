from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteCreateForm, NoteUpdateForm


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

    form = NoteUpdateForm()

    if request.method == "POST":
        form = NoteUpdateForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note:update-thought")
        return redirect("note:home")

    context = {
        'form': form
    }
    return render(request, "note_frontend/edit-thought.html", context)


def delete_thought(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return redirect("note:home")

    """
    TODO:
    - call the delete method on it
    - uhh?
    """

    return render(request, "note_frontend/confirm-delete.html")


def login(request):

    """
    TODO:
    - import the login form
    - implement post method
    - check to see if the login form is valid
    - if yes, validate, else; don't validate
    - uhh?
    """

    return render(request, "note_frontend/login.html")


def register(request):

    """
    TODO:
    - import the register form
    - implement post method
    - check to see if the register form is valid
    - if yes, validate, else; don't validate
    - uhh?
    """

    return render(request, "note_frontend/register.html")


def profile(request):

    """
    TODO:
    - import the profile form
    - add the request.user instance on the profile form
    - implement post method
    - check to see if the profile form is valid
    - if yes, validate, else; don't validate
    - uhh?
    """

    return render(request, "note_frontend/profile.html")
