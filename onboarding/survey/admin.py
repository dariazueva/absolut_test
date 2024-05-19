from django.contrib import admin

from survey.models import Answer, Question, TextResponse

admin.site.empty_value_display = 'Не задано'


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class TextResponseInline(admin.TabularInline):
    model = TextResponse
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Администратор для модели Question."""

    list_display = (
        'text',
        'question_type',
    )
    list_editable = (
        'question_type',
    )
    list_display_links = ('text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Администратор для модели Answer."""

    list_display = (
        'text',
        'question',
        'next_question',
    )
    list_editable = (
        'question',
        'next_question',
    )
    list_display_links = ('text',)


@admin.register(TextResponse)
class TextResponseAdmin(admin.ModelAdmin):
    """Администратор для модели TextResponse."""

    list_display = (
        'response',
        'question',
    )
    list_editable = (
        'question',
    )
    list_display_links = ('response',)
