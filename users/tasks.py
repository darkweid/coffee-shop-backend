from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from .models import CustomUser


@shared_task
def delete_inactive_users():
    """Delete users who are not active and were created more than 2 days ago."""
    threshold_date = now() - timedelta(days=2)
    deleted_count, _ = CustomUser.objects.filter(is_active=False, date_joined__lt=threshold_date).delete()
    return f'{deleted_count} inactive users deleted.'


# @shared_task
# def test_task():
#     """Task for testing celery worker"""
#     print("Celery test task executed!")
