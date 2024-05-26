from django.db import models


class Question(models.Model):
    """Модель вопроса."""

    TEXT = 'text'
    CHOICE = 'choice'
    CHECKBOX = 'checkbox'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (CHOICE, 'Choice'),
        (CHECKBOX, 'Checkbox'),
    ]

    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10,
                                     choices=QUESTION_TYPES,
                                     default='choice')
    next_question = models.ForeignKey('self', null=True, blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='previous_questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('text',)

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Модель ответа с выбором."""

    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    text = models.CharField(max_length=255)
    next_question = models.ForeignKey(Question, null=True, blank=True,
                                      on_delete=models.SET_NULL,
                                      related_name='answers_to_next')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ('question',)

    def __str__(self):
        return self.text


class TextResponse(models.Model):
    """Модель текстового ответа."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Текстовый ответ'
        verbose_name_plural = 'Текстовые ответы'
        ordering = ('question',)

    def __str__(self):
        return self.response


class CheckboxResponse(models.Model):
    """Модель ответа с галочкой."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.BooleanField()

    class Meta:
        verbose_name = 'Ответ с галочкой'
        verbose_name_plural = 'Ответы с галочкой'
        ordering = ('question',)

    def __str__(self):
        return self.response
