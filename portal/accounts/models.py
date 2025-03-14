from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name_ru = models.CharField(
        max_length=300, verbose_name=_("Имя на русском"), blank=True, null=True
    )
    first_name_kk = models.CharField(
        max_length=300, verbose_name=_("Имя на казахском"), blank=True, null=True
    )
    last_name_ru = models.CharField(
        max_length=300, verbose_name=_("Фамилия на русском"), blank=True, null=True
    )
    last_name_kk = models.CharField(
        max_length=300, verbose_name=_("Фамилия на казахском"), blank=True, null=True
    )
    surname_ru = models.CharField(
        max_length=300, verbose_name=_("Отчество на русском"), blank=True, null=True
    )
    surname_kk = models.CharField(
        max_length=300, verbose_name=_("Отчество на казахском"), blank=True, null=True
    )
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions granted to each of their groups."
        ),
        verbose_name=_("groups"),
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name=_("user permissions"),
    )

    def save(self, *args, **kwargs):
        if not self.pk:  # Если объект новый (создается впервые)
            if not self.first_name_ru:
                self.first_name_ru = self.first_name
            if not self.first_name_kk:
                self.first_name_kk = self.first_name
        super().save(*args, **kwargs)


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
        verbose_name="Расшарено с",
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
