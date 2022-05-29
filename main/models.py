from django.db import models


class Test(models.Model):
    fio = models.CharField('ФИО', max_length=100)
    group = models.CharField('Группа', max_length=100)
    result = models.IntegerField('Результат')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Результат теста'
        verbose_name_plural = 'Результаты тестов'
