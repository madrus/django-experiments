from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.conf import settings


def sendEmail():
    message = "Uw premieberekening is verzonden naar uw emailadres"

    try:
        email = EmailMessage(
            "Uw premieberekening",
            "De groeten van Movir",
            'admin@movir.local',
            ['andre@movir.local'],
            headers = {'Reply-To': settings.DEFAULT_FROM_EMAIL})
        email.send()

        #send_mail(
        #    'Subject here',
        #    'Here is the message.',
        #    'admin@movir.local',
        #    ['andre@movir.local'],
        #    fail_silently=False,
        #)
    except BadHeaderError:
        message = "Ongeldige email header"

    return message
