from . import models, mixins
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class MailingListListView(LoginRequiredMixin, generic.ListView):

    def get_queryset(self):
        return models.MailingList.objects.filter(owner=self.request.user)
