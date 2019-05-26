from django.conf import settings
from django.db import models
from django.urls import reverse

from uuid import uuid4


class MailingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mailing:manage", args=[self.id])

    def user_can_use_mailing_list(self, user):
        return user == self.owner


class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)

    class Meta:
        unique_together = "email", "mailing_list",

    def __str__(self):
        return self.email


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    subject = models.CharField(max_length=140)
    body = models.TextField()
    started = models.DateTimeField(default=None, null=True)
    finished = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.subject[:70]
