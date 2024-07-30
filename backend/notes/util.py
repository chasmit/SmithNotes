from .models import Note

def get_note_by_id_util(pk):
    notes = Note.objects.get(id=pk)
    return notes