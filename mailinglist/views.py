from . import models, mixins, forms

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MailingListListView(LoginRequiredMixin, generic.ListView):

    def get_queryset(self):
        return models.MailingList.objects.filter(owner=self.request.user)


class MailingListCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.MailingListForm
    template_name = "mailinglist/mailinglist_form.html"

    def get_initial(self):

        return {"owner": self.request.user.id}


class MailingListDeleteView(LoginRequiredMixin,
                            mixins.UserCanUseMailingList,
                            generic.DeleteView):
    model = models.MailingList
    success_url = reverse_lazy("mailinglist:list")
