from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from survey.models import Answer, Question, TextResponse


class CustomLoginView(LoginView):
    """Функция для входа пользователя."""

    template_name = 'login.html'


class CustomRegisterView(CreateView):
    """Функция для регистрации пользователя."""

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    """Функция для выхода пользователя."""

    template_name = 'logout.html'


@login_required
def survey_view(request, question_id=None):
    """Функция для анкетирования пользователя."""

    if question_id:
        question = get_object_or_404(Question, pk=question_id)
    else:
        question = Question.objects.first()
    if request.method == 'POST':
        if question.question_type == 'choice':
            selected_answer_id = request.POST.get('answer')
            selected_answer = get_object_or_404(Answer, pk=selected_answer_id)
            next_question = selected_answer.next_question
        elif question.question_type == 'text':
            text_response = request.POST.get('text_response')
            TextResponse.objects.create(question=question, response=text_response)
            next_question = question.next_question
        if next_question:
            return redirect('survey_question', question_id=next_question.id)
        else:
            return render(request, 'survey/complete_survey.html')
    return render(request, 'survey/home.html', {'question': question})
