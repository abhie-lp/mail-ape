from . import views
from django.urls import path, include

app_name = "mailinglist"

uuid_urls = [
    path("message/new/", views.CreateMessageView.as_view(),
         name="create_message"),
    path("message/", views.MessageDetailView.as_view(),
         name="view_message"),
    path("unsubscribe/", views.UnsubscribeView.as_view(), name="unsubscribe"),
    path("delete/", views.MailingListDeleteView.as_view(), name="delete"),
    path("manage/", views.MailingListDetailView.as_view(), name="manage"),
    path("subscribe/", views.SubscribeToMailingListView.as_view(),
         name="subscribe"),
    path("thankyou/", views.ThankYouForSubscribingView.as_view(),
         name="subscriber_thankyou"),
]

mailinglist_urls = [
    path("new/", views.MailingListCreateView.as_view(), name="create"),
    path("<uuid:pk>/", include(uuid_urls)),
]

urlpatterns = [
    path("subscribe/confirmation/<uuid:pk>/",
         views.ConfirmSubscriptionView.as_view(),
         name="confirm_subscription"),
    path("mailinglist/", include(mailinglist_urls)),
    path("", views.MailingListListView.as_view(), name="list"),
]
