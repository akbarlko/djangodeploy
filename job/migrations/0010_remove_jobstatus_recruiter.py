# Generated by Django 4.1.4 on 2022-12-20 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_jobstatus_recruiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobstatus',
            name='recruiter',
        ),
    ]
