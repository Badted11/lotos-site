from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название материала")
    description = models.TextField(verbose_name="Описание")
    application = models.TextField(verbose_name="Сфера применения", blank=True, null=True)
    usage = models.TextField(verbose_name="Способ применения", blank=True, null=True)
    advantages = models.TextField(verbose_name="Ключевые преимущества", blank=True, null=True)
    image = models.ImageField(upload_to='materials/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
