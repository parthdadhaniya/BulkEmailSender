# Generated by Django 5.0.2 on 2024-02-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkemailsender',
            name='email_file',
            field=models.FileField(upload_to='media', verbose_name='Email File'),
        ),
    ]
