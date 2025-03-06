from django.db import models


class HeaderImage(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name="Заголовок (русский)")
    title_kk = models.CharField(max_length=200, verbose_name="Заголовок (казахский)")
    description_ru = models.TextField(verbose_name="Описание (русский)")
    description_kk = models.TextField(verbose_name="Описание (казахский)")
    image = models.ImageField(upload_to="header_images/", verbose_name="Изображение")
    is_active = models.BooleanField(default=False, verbose_name="Активное изображение")

    def save(self, *args, **kwargs):
        if self.is_active:
            HeaderImage.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Изображение заголовка"
        verbose_name_plural = "Изображения заголовка"


class UsefulLink(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name="Название (русский)")
    title_kk = models.CharField(max_length=200, verbose_name="Название (казахский)")
    description_ru = models.TextField(verbose_name="Описание (русский)")
    description_kk = models.TextField(verbose_name="Описание (казахский)")
    image = models.ImageField(upload_to="useful_links/", verbose_name="Изображение")
    url = models.URLField(verbose_name="Ссылка")
    is_active = models.BooleanField(default=False, verbose_name="Активная ссылка")

    def __str__(self):
        return self.title_ru

    class Meta:
        verbose_name = "Полезная ссылка"
        verbose_name_plural = "Полезные ссылки"
