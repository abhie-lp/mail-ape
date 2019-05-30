from django.conf import settings
from django.template import engines, Context
from django.urls import reverse
from django.core.mail import send_mail

CONFIRM_SUBSCRIPTION_HTML = "mailinglist/emails/confirmation.html"
CONFIRM_SUBSCRIPTION_TEXT = "mailinglist/emails/confirmation.txt"


class EmailTemplateContext(Context):

    @staticmethod
    def make_link(path):
        return settings.MAILINGLIST_LINK_DOMAIN + path

    def __init__(self, subscriber, dict_=None, **kwargs):
        if dict_ is None:
            dict_ = {}
        email_ctx = self.common_context(subscriber)
        email_ctx.update(dict_)
        super().__init__(email_ctx, **kwargs)

    def common_context(self, subscriber):
        subscriber_pk_kwargs = {"pk": subscriber.id}
        unsubscribe_path = reverse("mailinglist:unsubscribe",
                                   kwargs=subscriber_pk_kwargs)

        return {
            "subscriber": subscriber,
            "mailing_list": subscriber.mailing_list,
            "unsubscribe_link": self.make_link(unsubscribe_path),
        }


def send_confirmation_email(subscriber):
    mailing_list = subscriber.mailing_list
    confirmation_link = EmailTemplateContext.make_link(
        reverse("mailinglist:confirm_subscription", args=[subscriber.id])
    )

    context = EmailTemplateContext(
        subscriber,
        {"confirmation_link": confirmation_link}
    )

    subject = "Confirming subscription to {}".format(mailing_list.name)

    dt_engine = engines["django"].engine
    text_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_TEXT)
    text_body = text_body_template.render(context=context)
    html_body_template = dt_engine.get_template(CONFIRM_SUBSCRIPTION_HTML)
    html_body = html_body_template.render(context=context)

    send_mail(subject=subject,
              message=text_body,
              from_email=settings.MAILINGLIST_FROM_EMAIL,
              recipient_list=[subscriber.email],
              fail_silently=False,
              html_message=html_body)
