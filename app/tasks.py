import os
import smtplib
from celery import shared_task
from django.conf import settings
from email.message import EmailMessage


# @shared_task
def email_send(email_list, email_subject, email_body, email_file):
    # Connect to Gmail's SMTP server
    with smtplib.SMTP(settings.SMTP_SERVERE, int(settings.SMTP_SERVERE_PORT)) as smtp:
        smtp.starttls()
        smtp.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)

        # Create the email
        email = EmailMessage()
        email["Subject"] = email_subject
        email["From"] = settings.EMAIL_FROM
        email["To"] = email_list
        email.set_content(email_body)

        # Attach the PDF file
        with open(f"media\{email_file.name}", "rb") as pdf_file:
            content = pdf_file.read()
            email.add_attachment(
                content,
                maintype="application",
                subtype="octet-stream",
                filename=email_file.name,
            )

        # Send the email
        smtp.send_message(email)
    return True
