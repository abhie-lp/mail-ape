from . import models, mixins, forms

from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
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


class MailingListDetailView(LoginRequiredMixin,
                            mixins.UserCanUseMailingList,
                            generic.DetailView):
    model = models.MailingList


class SubscribeToMailingListView(generic.CreateView):
    form_class = forms.SubscriberForm
    template_name = "mailinglist/subscriber_form.html"

    def get_initial(self):
        return {
            "mailing_list": self.kwargs.get("pk")
        }

    def get_success_url(self):
        return reverse("mailinglist:subscriber_thankyou",
                       args=[self.object.mailing_list.id])

    def get_context_data(self, **kwargs):
        ctx = super(SubscribeToMailingListView, self).get_context_data(**kwargs)
        mailing_list_id = self.kwargs.get("pk")
        ctx["mailing_list"] = get_object_or_404(models.MailingList,
                                                id=mailing_list_id)

        return ctx


class ThankYouForSubscribingView(generic.TemplateView):

    template_name = "mailinglist/subscription_thankyou.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["mailinglist"] = get_object_or_404(models.MailingList,
                                               id=self.kwargs.get("pk"))
        return ctx


class ConfirmSubscriptionView(generic.DetailView):
    model = models.Subscriber
    template_name = "mailinglist/confirm_subscription.html"

    def get_object(self, queryset=None):
        subscriber = super().get_object(queryset=queryset)
        subscriber.confirmed = True
        subscriber.save()
        return subscriber
