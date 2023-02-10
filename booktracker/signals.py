from django.db.models.signals import pre_save
from django.dispatch import receiver
from booktracker.models import BookUsers, BookStatus


@receiver(pre_save, sender=BookUsers)
def process_status(instance: BookUsers,  **kwargs):
    if instance.status_id is None:
        instance.status = BookStatus.objects.get(name='Хочу прочитать')
