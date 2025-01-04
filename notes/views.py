from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Note
from .forms import NoteForm

def is_staff(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff)
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes')  # Redirect to the notes page
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

@login_required
@user_passes_test(is_staff)
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')  # Redirect to the notes page
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/add_note.html', {'form': form, 'is_edit': True})


@login_required
@user_passes_test(is_staff)
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')  # Redirect to the notes page
    return render(request, 'notes/delete_note.html', {'note': note})

def notes(request):
    notes = Note.objects.order_by('-created_at')
    return render(request, 'notes/notes.html', {'notes': notes})
