# Generated by Django 5.1.6 on 2025-03-13 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_task_completed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Расшарено с'),
        ),
    ]
