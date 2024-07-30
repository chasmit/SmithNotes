from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg'])], required=False)
                                                                     
    class Meta:
        model = Note
        fields = ['id', 'header', 'body', 'image', 'created_date', 'last_modified']