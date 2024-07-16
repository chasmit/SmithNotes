from rest_framework.serializers import Serializer
from .models import Note

class NoteSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'