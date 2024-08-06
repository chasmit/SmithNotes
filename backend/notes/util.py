from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer

def get_note_by_id_util(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)