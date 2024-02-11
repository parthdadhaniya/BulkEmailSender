from django.db import models

# Create your models here.


class BulkEmailSender(models.Model):
    task_name = models.CharField(max_length=50, verbose_name="Task Name")
    email_list = models.TextField(verbose_name="Email List")
    email_subject = models.CharField(max_length=255, verbose_name="Email Subject")
    email_body = models.TextField(verbose_name="Email Body")
    email_file = models.FileField(verbose_name="Email File", upload_to="media")

    def __str__(self):
        return str(self.task_name)
