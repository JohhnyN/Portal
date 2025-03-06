from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Department(MPTTModel):
    department_ru = models.CharField(
        max_length=255, verbose_name=_("Название на русском")
    )
    department_kk = models.CharField(
        max_length=255, verbose_name=_("Название на казахском")
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_departments",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Создано пользователем"),
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="updated_departments",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Обновлено пользователем"),
    )

    is_deleted = models.BooleanField(default=False, verbose_name=_("Удалено"))
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Дата удаления")
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="deleted_departments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Удалено пользователем"),
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        help_text=_("Родительское подразделение"),
        verbose_name=_("Родительское подразделение"),
    )

    class MPTTMeta:
        order_insertion_by = []

    class Meta:
        verbose_name = _("Подразделение")
        verbose_name_plural = _("Подразделения")

    def __str__(self):
        return self.department_ru


class CityPhoneNumber(models.Model):
    number = models.CharField(max_length=20, verbose_name=_("Городской номер телефона"))

    class Meta:
        verbose_name = _("Городской номер телефона")
        verbose_name_plural = _("Городские номера телефонов")

    def __str__(self):
        return self.number


class Employee(models.Model):
    name_ru = models.CharField(max_length=300, verbose_name=_("ФИО на русском"))
    name_kk = models.CharField(max_length=300, verbose_name=_("ФИО на казахском"))
    position_ru = models.CharField(
        max_length=100, verbose_name=_("Должность на русском")
    )
    position_kk = models.CharField(
        max_length=100, verbose_name=_("Должность на казахском")
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
        verbose_name=_("Подразделение"),
    )
    email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    city_phone_number = models.ForeignKey(
        CityPhoneNumber,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
        verbose_name=_("Городской номер телефона"),
    )
    mobile_number = models.CharField(
        max_length=20, verbose_name=_("Сотовый номер"), blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="photos/", blank=True, null=True, verbose_name=_("Фото")
    )
    order = models.PositiveIntegerField(
        default=20,
        help_text=_("Порядковый номер для сортировки сотрудников"),
        verbose_name=_("Порядковый номер для сортировки сотрудников"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_employees",
        verbose_name=_("Создано пользователем"),
    )

    updated_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Дата обновления")
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_employees",
        verbose_name=_("Обновлено пользователем"),
    )

    is_deleted = models.BooleanField(default=False, verbose_name=_("Удалено"))
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Дата удаления")
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deleted_employees",
        verbose_name=_("Удалено пользователем"),
    )

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")
        ordering = ["order", "name_ru"]

    def __str__(self):
        return self.name_ru


@receiver(pre_save, sender=Employee)
def set_updated_at(sender, instance, **kwargs):
    if instance.pk:
        instance.updated_at = timezone.now()


@receiver(pre_save, sender=Department)
def set_department_updated_at(sender, instance, **kwargs):
    if instance.pk:
        instance.updated_at = timezone.now()
