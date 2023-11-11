from celery import shared_task
from datetime import timedelta
from .models import CurrencyConversion
from django.utils import timezone

@shared_task
def update_conversion_status():
 
    conversions = CurrencyConversion.objects.filter(
        status='temporary',
        created_at__lte=timezone.now() - timedelta(seconds=1)
    )

    for conversion in conversions:
        conversion.status = 'permanent'
        conversion.save()

@shared_task
def schedule_update_conversion_status():
    """
    Celery periodic task to schedule the update_conversion_status task.
    """
    update_conversion_status.apply_async(eta=timezone.now() + timezone.timedelta(seconds=1))
