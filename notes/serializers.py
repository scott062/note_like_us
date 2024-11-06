from rest_framework import serializers
from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'is_archived',
            'positive_sentiment',
            'negative_sentiment',
            'neutral_sentiment',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
            'is_archived',
            'positive_sentiment',
            'negative_sentiment',
            'neutral_sentiment',
        ]

