from . import views
from django.urls import path

app_name = "mailinglist"

urlpatterns = [
    path("", views.MailingListListView.as_view(), name="list"),
]
