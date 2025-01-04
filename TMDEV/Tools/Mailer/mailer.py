from django.core.mail import send_mail
from django.conf import settings


class Mailer:
    def __init__(self):
        pass

    def format_email_text(self):
        return 1

    def send_email(self, subject, content, destination):
        """Send email

        Send email using SMTP
        The sender and SMTP is set in settings.py

        For debugging:
        - check: https://gist.github.com/andreagrandi/7027319
        - use a debug smtp: python3 -m smtpd -n -c DebuggingServer localhost:1025

        Check: https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
        """

        # Send email
        try:
            send_mail(
                subject=subject, message=content, from_email=settings.EMAIL_HOST_USER, recipient_list=[destination]
            )
        except Exception as e:
            print(f"Crap: {e}")
