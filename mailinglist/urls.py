from . import views
from django.urls import path, include

app_name = "mailinglist"

mailinglist_urls = [
    path("new/", views.MailingListCreateView.as_view(), name="create"),
]

urlpatterns = [
    path("mailinglist/", include(mailinglist_urls)),
    path("", views.MailingListListView.as_view(), name="list"),
]
