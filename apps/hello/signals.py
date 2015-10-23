from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from.models import EventLog


@receiver(post_save)# flake8: noqa
def model_create_or_update(sender, created,  **kwargs):
    if str(sender.__name__) in ("Mycard", "RequestInfo"):
        EventLog.objects.create(event='Created' if created else 'Updated',
                                model=sender.__name__)


@receiver(post_delete)# flake8: noqa
def model_delete(sender, **kwargs):
    if str(sender.__name__) in ("Mycard", "RequestInfo"):
        EventLog.objects.create(event='Deleted', model=sender.__name__)
