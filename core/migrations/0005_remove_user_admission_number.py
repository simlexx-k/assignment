# Generated by Django 5.0.3 on 2024-04-02 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_submission_feedback_submission_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admission_number',
        ),
    ]