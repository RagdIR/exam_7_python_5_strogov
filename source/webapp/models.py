from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=300, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания вопроса")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    variant = models.CharField(max_length=300, null=False, blank=False, verbose_name='Варианты ответов')
    poll = models.ForeignKey('webapp.Poll', related_name='poll',
                               on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return self.variant

    class Meta:
        verbose_name = 'Текст варианта'
        verbose_name_plural = 'Тексты вариантов'


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='poll',
                               on_delete=models.CASCADE, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания ответа")
    choice = models.ForeignKey('webapp.Choice', related_name='choice',
                               on_delete=models.CASCADE, verbose_name='Вариант')
