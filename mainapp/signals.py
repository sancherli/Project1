from django.db.models import Avg, Count
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


def refresh_app_rating(app_id):
    stats = Review.objects.filter(app_id=app_id).aggregate(
        avg=Avg('rating'),
        count=Count('id'),
    )

    from .models import App

    App.objects.filter(id=app_id).update(
        rating_avg=stats['avg'] or 0,
        rating_count=stats['count'],
    )


@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    refresh_app_rating(instance.app_id)


@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    refresh_app_rating(instance.app_id)