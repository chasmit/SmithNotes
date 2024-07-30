from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer
from .util import get_note_by_id_util


def get_routes(request):
    routes = [
        '/backend/notes/',
        '/backend/notes/create/',
        '/backend/notes/<int:pk>/',
        '/backend/notes/<int:pk>/modify/',
        '/backend/notes/<int:pk>/delete/'
    ]
    
    return Response(routes)


@api_view(['GET'])
def get_notes(request):
    notes = Note.objects.all().order_by('-last_modified')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_note_by_id(request, pk):
    return get_note_by_id_util(pk)


@api_view(['POST'])
def add_note(request):
    data = request.data

    note = Note.objects.create(
        header = data['header'],
        body = data['body'],
        image = data['image']
    )

    serializer = NoteSerializer(note, {'request': request}, many=False)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def modify_note(request, pk):
    data = request.data
    note = get_note_by_id_util(data['id'])
    print(data)

    note = Note.objects.update(
        header = data['header'],
        body = data['body'],
        image = data['image']
    )

    serializer = NoteSerializer(note, {'request': request}, many=False)
    if serializer.is_valid():
        serializer.save()

        return Response(status.HTTP_200_OK)
    
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_note(pk):
    note = get_note_by_id(pk)
    note.delete()

    return Response(status.HTTP_200_OK)
