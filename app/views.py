import os
import uuid
from app.tasks import email_send
from django.shortcuts import render
from django.http import HttpResponse
from app.helpers import email_lists
from django.contrib import messages
from app.models import BulkEmailSender

# Create your views here.


def index(request):
    try:
        if request.method == "POST":
            task_name = request.POST.get("task_name")
            email_list = request.POST.get("email_list")
            email_subject = request.POST.get("email_subject")
            email_body = request.POST.get("email_body")

            # Get file data
            email_file = request.FILES.get("email_file")
            # Generate a unique identifier
            unique_identifier = str(uuid.uuid4()).replace("-", "")[:8]
            # Split the original file name and its extension
            file_name, file_extension = os.path.splitext(email_file.name)
            # Concatenate task name and unique identifier
            task_name_with_uid = f"{task_name}_{unique_identifier}"
            # Generate a unique identifier for the file name
            file_name_uid = str(uuid.uuid4()).replace("-", "")[:8]
            # Concatenate original file name and unique identifier
            file_name_with_uid = f"{file_name}_{file_name_uid}{file_extension}"
            with open(file_name_with_uid, "wb") as file:
                for chunk in email_file.chunks():
                    file.write(chunk)
            data = BulkEmailSender(
                task_name=task_name_with_uid,
                email_list=email_list,
                email_subject=email_subject,
                email_body=email_body,
                email_file=file_name_with_uid,
            )
            data.save()
            email_data = BulkEmailSender.objects.get(task_name=task_name_with_uid)
            email = email_lists(email_data.email_list)
            subject = email_data.email_subject
            body = email_data.email_body
            file_path = email_data.email_file

            email_send.apply_async(
                args=[
                    email,
                    subject,
                    body,
                    f"/home/parth/Desktop/BulkEmailSender/{file_path}",
                ]
            )
            messages.success(request, "Email sent successfully")
        return render(request, "index.html")
    except Exception as e:
        print(e)
        return render(request, "index.html")
