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
