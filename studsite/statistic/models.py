from django.db import models


class ModelInstancesChange(models.Model):
    app_label = models.CharField(verbose_name=u'Приложение', max_length=50)
    model_name = models.CharField(verbose_name=u'Модель', max_length=50)
    change_time = models.DateTimeField(
        verbose_name=u'Время изменения', auto_now_add=True)
    change_type = None

    class Meta:
        verbose_name = u''
        verbose_name_plural = u''

    def __str__(self):
        return u''

    def save(self):
        super().save()
