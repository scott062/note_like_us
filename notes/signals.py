from django.db.models.signals import post_save
from django.dispatch import receiver
from notes.models import Note
from transformers import pipeline


@receiver(post_save, sender=Note)
def calculate_sentiment_score(sender, instance, created, **kwargs):
    if not instance:
        return

    # Prevent recursive call on saves
    if hasattr(instance, '_dirty'):
        return

    try:
        instance._dirty = True # Avoid recursive loop on post_save

        pipe = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
        result = pipe(instance.content, top_k=3)
        scores = parse_scores_response(result)

        Note.objects.filter(id=instance.id).update(
                negative_sentiment=scores[0],
                neutral_sentiment=scores[1],
                positive_sentiment=scores[2]
            )
    except Exception as e:
        print(f"Error calculating sentiment score: {e}")
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

