from celery import shared_task
from django.core.mail import EmailMessage
import os

from django.core.mail import EmailMessage, BadHeaderError
from django.utils.html import strip_tags


@shared_task
def email_send(email, subject, body, file_path):
    # Print file_path for debugging
    print("File Path:", file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Check if the file is not empty
        if os.path.getsize(file_path) > 0:
            with open(file_path, "rb") as file:
                file_content = file.read()  # Read the file content
                email_message = EmailMessage(subject, strip_tags(body), to=email)
                email_message.attach_file(file_path)
                try:
                    email_message.send()
                    os.remove(file_path)
                    print("Email sent successfully.")
                except BadHeaderError as e:
                    print("Invalid header found:", e)
                    print("Email not sent.")
        else:
            print("File is empty:", file_path)
            print("Email not sent.")
    else:
        print("File not found:", file_path)
        print("Email not sent.")
