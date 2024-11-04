from django.db import models
from django.contrib.auth.models import User
import uuid

class Note(models.Model):
    # Note Core Functions
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    # Locking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Alternative Deletion
    is_archived = models.BooleanField(default=False)

    # Sentiment Model Scores
    positive_sentiment = models.FloatField(null=True, blank=True)
    negative_sentiment = models.FloatField(null=True, blank=True)
    neutral_sentiment = models.FloatField(null=True, blank=True)

