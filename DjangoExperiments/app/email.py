from django.core.mail import send_mail
from django.conf import settings

def send_email(request):

    send_mail(
        'Subject here',
        'Here is the message.',
        'admin@movir.local',
        ['andre@movir.local'],
        fail_silently=False,
    )