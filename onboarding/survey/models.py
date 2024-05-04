from django.db import models


class BusinessType(models.Model):
    """Модель типа бизнеса."""

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тип бизнеса'
        verbose_name_plural = 'Типы бизнеса'
        ordering = ('name',)

    def __str__(self):
        return self.name


class BusinessDirection(models.Model):
    """Модель направления бизнеса."""

    name = models.CharField(max_length=100)
    business_type = models.ForeignKey(BusinessType,
                                      on_delete=models.CASCADE,
                                      related_name='directions')

    class Meta:
        verbose_name = 'Направление бизнеса'
        verbose_name_plural = 'Направления бизнеса'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Survey(models.Model):
    """Модель опроса."""

    title = models.CharField(max_length=255,
                             null=True,
                             blank=True)
    business_type = models.ForeignKey(BusinessType,
                                      on_delete=models.CASCADE,
                                      related_name='surveys')
    business_direction = models.ForeignKey(BusinessDirection,
                                           on_delete=models.CASCADE,
                                           related_name='surveys')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопроса."""

    text = models.CharField(max_length=255)
    dynamic = models.BooleanField(default=False)
    parent_question = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=True)
    survey = models.ForeignKey(Survey,
                               on_delete=models.CASCADE,
                               related_name='questions',
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('text',)

    def __str__(self):
        return self.text


class Choice(models.Model):
    """Модель варианта ответа."""

    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='choices')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
        ordering = ('text',)

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Модель ответа."""

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('text',)

    def __str__(self):
        return self.text


class QuestionBranch(models.Model):
    """Модель следующего вопроса."""

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='branches')
    choice = models.ForeignKey(Choice,
                               on_delete=models.CASCADE)
    next_question = models.ForeignKey(Question,
                                      on_delete=models.CASCADE,
                                      related_name='next_questions')

    class Meta:
        verbose_name = 'Следующий вопрос'
        verbose_name_plural = 'Следующие вопросы'
        ordering = ('next_question',)

    def __str__(self):
        return f"{self.question} -> {self.choice} -> {self.next_question}"
