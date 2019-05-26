from . import models
from django.contrib import admin


@admin.register(models.MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = "id", "name", "owner",


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = "id", "email", "mailing_list", "confirmed",
    list_editable = "confirmed",


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = "id", "mailing_list", "subject",
