from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    custom_first_name = models.CharField(
        max_length=300, verbose_name=_("Имя"), blank=True, null=True, default=""
    )
    custom_last_name = models.CharField(
        max_length=300, verbose_name=_("Фамилия"), blank=True, null=True, default=""
    )
    surname = models.CharField(
        max_length=300, verbose_name=_("Отчество"), blank=True, null=True, default=""
    )
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return (
            f"{self.custom_last_name} {self.custom_first_name} {self.surname}"
            if self.custom_last_name and self.custom_first_name
            else self.username
        )


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Низкий"),
        ("medium", "Средний"),
        ("high", "Высокий"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание задачи")
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="medium",
        verbose_name="Приоритет",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_completed = models.BooleanField(default=False, verbose_name="Завершена")
    completed_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Время завершения"
    )
    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="shared_tasks",
        blank=True,
        verbose_name="Делегировать задачу сотруднику(ам)",
    )

    def __str__(self):
        return self.title

    def has_comments_from_user(self, user):
        return self.comments.filter(user=user).exists()

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Комментарий от {self.user.username} к задаче {self.task.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
