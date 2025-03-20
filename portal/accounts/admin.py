from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task, Comment
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "custom_first_name",
        "custom_last_name",
        "is_staff",
        "photo_thumbnail",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "custom_first_name",
                    "custom_last_name",
                    "surname",
                    "email",
                    "photo",
                    "photo_display",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "custom_first_name",
                    "custom_last_name",
                    "surname",
                    "email",
                    "photo",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    readonly_fields = ["photo_display"]

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="150" />',
                obj.photo.url,
            )
        return "Нет фото"

    photo_thumbnail.short_description = "Фото"

    def photo_display(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="300" />',
                obj.photo.url,
            )
        return "Нет фото"

    photo_display.short_description = "Фото"


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "is_completed", "created_at", "updated_at")
    list_filter = ("is_completed", "created_at", "updated_at")
    search_fields = ("title", "description", "user__username")
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("task", "user", "text", "created_at")
    list_filter = ("created_at",)
    search_fields = ("task__title", "user__username", "text")
    ordering = ("-created_at",)
