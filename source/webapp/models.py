from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=300, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создания опроса")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    variant = models.CharField(max_length=300, null=False, blank=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='poll',
                               on_delete=models.PROTECT, verbose_name='Вопрос')

    def __str__(self):
        return self.variant

    class Meta:
        verbose_name = 'Текст варианта'
        verbose_name_plural = 'Тексты вариантов'