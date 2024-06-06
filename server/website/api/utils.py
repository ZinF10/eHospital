from django.core.mail import send_mail
from core.settings import base


def send_custom_email(subject, message, recipients):
    send_mail(subject=subject, message=message, from_email=base.DEFAULT_FROM_EMAIL,
              recipient_list=recipients, fail_silently=False)


def generate_reset_code(user):
    import random, string
    reset_code = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=7))
    user.reset_code = reset_code
    user.save()
    return reset_code
