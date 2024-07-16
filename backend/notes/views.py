from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def get_all_notes(request):
    notes = Note.objects.all().order_by('-last_modified')
    serializer = NoteSerializer(notes, {'request': request}, many=True)
    return Response(serializer.data)


def get_note_by_id(request, id):
    try:
        note = Note.objects.get(uuid=id)
    except Note.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_new_note(request):
    data = request.data
    note = Note.objects.create(
        header=data['header'],
        body=data['body'],
        image=data['image']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def modify_note(request, id):
    note = get_note_by_id(id)
    
    data = request.data
    serializer = NoteSerializer(note, data, {'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_note(request, id):
    note = get_note_by_id(id)
    note.delete()
    return Response(status.HTTP_200_OK)
