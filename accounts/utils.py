from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from datetime import timedelta

def send_simple_email(user_email):
    send_mail(
        subject="Django email sinovi",
        message="Bu test email",
        from_email="orinboyevshohjahon16@gmail.com",
        recipient_list=[EMAIL_HOST_USER,user_email],
        fail_silently=False,
    )

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_html_email(user_email, user_name):
    subject = "HTML email sinovi"

    context = {
        "subject": subject,
        "user_name": user_name,
        "message": (
            "Sizga muhim ma’lumot yuborildi. "
            "Batafsil tanishish uchun quyidagi tugmani bosing."
        ),
        "button_text": "Batafsil ma’lumot",
        "button_url": "https://ustudy.uz",
    }

    html_content = render_to_string(
        "emails/welcome_email.html",
        context,
    )

    text_content = (
        f"Salom, {user_name}!\n\n"
        f"{context['message']}\n\n"
        f"Havola: {context['button_url']}\n\n"
        "Hurmat bilan,\n"
        "Ustudy IT Akademiyasi"
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email],
    )

    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)
def get_code():
    import random
    data=random.randint(100000,999999)
    return data

def get_expiry_date():
    return timezone.now() + timedelta(minutes=2)