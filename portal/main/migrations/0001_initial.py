# Generated by Django 5.1.6 on 2025-03-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Заголовок (русский)')),
                ('title_kk', models.CharField(max_length=200, verbose_name='Заголовок (казахский)')),
                ('description_ru', models.TextField(verbose_name='Описание (русский)')),
                ('description_kk', models.TextField(verbose_name='Описание (казахский)')),
                ('image', models.ImageField(upload_to='header_images/', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активное изображение')),
            ],
            options={
                'verbose_name': 'Изображение заголовка',
                'verbose_name_plural': 'Изображения заголовков',
            },
        ),
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, verbose_name='Название (русский)')),
                ('title_kk', models.CharField(max_length=200, verbose_name='Название (казахский)')),
                ('description_ru', models.TextField(verbose_name='Описание (русский)')),
                ('description_kk', models.TextField(verbose_name='Описание (казахский)')),
                ('image', models.ImageField(upload_to='useful_links/', verbose_name='Изображение')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активная ссылка')),
            ],
            options={
                'verbose_name': 'Полезная ссылка',
                'verbose_name_plural': 'Полезные ссылки',
            },
        ),
    ]
