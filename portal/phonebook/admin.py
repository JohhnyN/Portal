from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from .models import Department, CityPhoneNumber, Employee


@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin, ImportExportModelAdmin):
    list_display = (
        "department_ru",
        "department_kk",
        "created_at",
        "updated_at",
        "is_deleted",
    )
    list_filter = ("is_deleted", "created_at", "updated_at")
    search_fields = ("department_ru", "department_kk")


@admin.register(CityPhoneNumber)
class CityPhoneNumberAdmin(ImportExportModelAdmin):
    list_display = ("number",)
    search_fields = ("number",)


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = (
        "name_ru",
        "position_ru",
        "department",
        "photo_thumbnail",
        "email",
        "order_display",
        "created_at",
        "updated_at",
        "is_deleted",
    )
    list_filter = ("department", "is_deleted", "created_at", "updated_at")
    search_fields = (
        "name_ru",
        "name_kk",
        "position_ru",
        "position_kk",
    )
    ordering = ("order",)
    readonly_fields = (
        "photo_display",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "deleted_by",
        "deleted_at",
    )

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "Нет фото"

    photo_thumbnail.short_description = "Фото"

    def order_display(self, obj):
        return obj.order

    order_display.short_description = "Номер"

    def photo_display(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="300" />', obj.photo.url)
        return "Нет фото"

    photo_display.short_description = "Фото"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name_ru",
                    "name_kk",
                    "position_ru",
                    "position_kk",
                    "department",
                    "email",
                    "city_phone_number",
                    "mobile_number",
                    "order",
                    "photo",
                    "photo_display",
                )
            },
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "created_by",
                    "created_at",
                    "updated_by",
                    "updated_at",
                    "deleted_by",
                    "deleted_at",
                    "is_deleted",
                ),
                "classes": ("collapse",),
            },
        ),
    )
