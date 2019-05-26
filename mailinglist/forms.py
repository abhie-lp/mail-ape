from . import models
from django import forms


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = models.Subscriber
        fields = "mailing_list", "email",
        widgets = {"mailing_list": forms.HiddenInput()}

    def __init__(self, **kwargs):
        super(SubscriberForm, self).__init__(**kwargs)
        self.fields["mailing_list"].disabled = True


class MessageForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "mailing_list", "subject", "body",
        widgets = {"mailing_list": forms.HiddenInput()}

    def __init__(self, **kwargs):
        super(MessageForm, self).__init__(**kwargs)
        self.fields["mailing_list"].disabled = True


class MailingListForm(forms.ModelForm):

    class Meta:
        model = models.MailingList
        fields = "name", "owner",
        widgets = {"owner": forms.HiddenInput()}

    def __init__(self, **kwargs):
        super(MailingListForm, self).__init__(**kwargs)
        self.fields["owner"].disabled = True
