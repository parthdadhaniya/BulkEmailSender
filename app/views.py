from app.tasks import email_send
from django.shortcuts import render, redirect
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
            email_file = request.FILES.get("email_file")
            data = BulkEmailSender(
                task_name=task_name,
                email_list=email_list,
                email_subject=email_subject,
                email_body=email_body,
                email_file=email_file,
            )
            data.save()
            list_of_email = email_lists(email_list)
            result = email_send(list_of_email, email_subject, email_body, email_file)
            messages.success(request, "Email sent successfully")
        return render(request, "index.html")
    except Exception as e:
        print(e)
