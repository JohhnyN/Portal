from django.contrib import admin
from django.utils.html import format_html
from .models import HeaderImage, UsefulLink


@admin.register(HeaderImage)
class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "description_ru", "image_thumbnail", "is_active")
    list_editable = ("is_active",)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "Нет фото"

    image_thumbnail.short_description = "Фото"

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="300" />', obj.image.url)
        return "Нет фото"

    image_display.short_description = "Фото"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title_ru",
                    "title_kk",
                    "description_ru",
                    "description_kk",
                    "image",
                    "image_display",
                    "is_active",
                )
            },
        ),
    )

    readonly_fields = ("image_display",)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            HeaderImage.objects.filter(is_active=True).update(is_active=False)
        super().save_model(request, obj, form, change)


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "description_ru", "image_thumbnail", "url", "is_active")
    list_editable = ("is_active",)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" />', obj.image.url)
        return "Нет фото"

    image_thumbnail.short_description = "Фото"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title_ru",
                    "title_kk",
                    "description_ru",
                    "description_kk",
                    "image",
                    "url",
                    "is_active",
                )
            },
        ),
    )

    readonly_fields = ("image_thumbnail",)
