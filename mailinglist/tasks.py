from . import emails
from celery import shared_task


@shared_task
def send_confirmation_email_to_subscriber(subscriber_id):
    from .models import Subscriber

    subscriber = Subscriber.objects.get(id=subscriber_id)
    emails.send_confirmation_email(subscriber)
