from rest_framework import serializers

from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'created_on']