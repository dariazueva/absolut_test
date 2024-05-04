from django.contrib import admin

from survey.models import (BusinessType,
                           BusinessDirection,
                           Survey,
                           Question,
                           Choice,
                           Answer,
                           QuestionBranch)

admin.site.empty_value_display = 'Не задано'


class BusinessTypeInline(admin.TabularInline):
    model = BusinessType
    extra = 1


class BusinessDirectionInline(admin.TabularInline):
    model = BusinessDirection
    extra = 1


class SurveyInline(admin.TabularInline):
    model = Survey
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    """Администратор для модели BusinessType."""

    list_display = (
        'name',
    )
    list_display_links = ('name',)


@admin.register(BusinessDirection)
class BusinessDirectionAdmin(admin.ModelAdmin):
    """Администратор для модели BusinessDirection."""

    list_display = (
        'name',
        'business_type',
    )
    list_editable = (
        'business_type',
    )
    list_display_links = ('name',)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Администратор для модели Survey."""

    list_display = (
        'title',
        'business_type',
        'business_direction',
    )
    list_editable = (
        'business_type',
        'business_direction',
    )
    list_display_links = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Администратор для модели Question."""

    list_display = (
        'text',
        'dynamic',
        'parent_question',
        'survey',
    )
    list_editable = (
        'dynamic',
        'parent_question',
        'survey',
    )
    list_display_links = ('text',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """Администратор для модели Choice."""

    list_display = (
        'text',
        'question',
    )
    list_editable = (
        'question',
    )
    list_display_links = ('text',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Администратор для модели Answer."""

    list_display = (
        'text',
        'question',
    )
    list_editable = (
        'question',
    )
    list_display_links = ('text',)


@admin.register(QuestionBranch)
class QuestionBranchAdmin(admin.ModelAdmin):
    """Администратор для модели QuestionBranch."""

    list_display = (
        'choice',
        'question',
        'next_question',
    )
    list_editable = (
        'question',
        'next_question',
    )
    list_display_links = ('choice',)
