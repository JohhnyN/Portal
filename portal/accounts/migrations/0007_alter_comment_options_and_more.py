# Generated by Django 5.1.6 on 2025-03-19 05:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_comment'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name_kk',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name_ru',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name_kk',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name_ru',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='surname_kk',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='surname_ru',
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='task',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Делегировать задачу сотруднику(ам)'),
        ),
    ]
