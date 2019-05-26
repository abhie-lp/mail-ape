from . import views
from django.urls import path, include

app_name = "mailinglist"

uuid_urls = [
    path("delete/",
         views.MailingListDeleteView.as_view(),
         name="delete"),
    path("manage/", views.MailingListDetailView.as_view(), name="manage"),
]

mailinglist_urls = [
    path("new/", views.MailingListCreateView.as_view(), name="create"),
    path("<uuid:pk>/", include(uuid_urls)),
]

urlpatterns = [
    path("mailinglist/", include(mailinglist_urls)),
    path("", views.MailingListListView.as_view(), name="list"),
]
