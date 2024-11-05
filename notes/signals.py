import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from notes.models import Note
from note_like_us.settings import SENTIMENT_API_TOKEN


@receiver(post_save, sender=Note)
def calculate_sentiment_score(sender, instance, created, **kwargs):
    if not instance:
        return

    # Prevent recursive call on saves
    if hasattr(instance, '_dirty'):
        return

    api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    payload = {
        "inputs": instance.content,
    }
    headers = {"Authorization": f"Bearer {SENTIMENT_API_TOKEN}"}

    try:
        instance._dirty = True
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        scores = parse_scores_response(response.json()[0])

        Note.objects.filter(id=instance.id).update(
                negative_sentiment=scores[0],
                neutral_sentiment=scores[1],
                positive_sentiment=scores[2]
            )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sentiment score: {e}")
    finally:
        del instance._dirty


def parse_scores_response(data):
    pos = None
    neg = None
    neu = None
    for obj in data:
        score = obj.get("score")
        if obj.get("label") == "LABEL_0":
            neg = score
        if obj.get("label") == "LABEL_1":
            neu = score
        if obj.get("label") == "LABEL_2":
            pos = score
    return neg, neu, pos

