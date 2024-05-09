from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from survey.models import Answer, BusinessDirection, BusinessType, Question


class SurveyView(LoginRequiredMixin, TemplateView):
    """Функция для анкетирования."""

    template_name = 'survey/home.html'

    def get_questions(self):
        return Question.objects.all().order_by('id')

    def get_business_types(self):
        return BusinessType.objects.all()

    def get_business_directions(self, business_type_id):
        if business_type_id:
            answer = Answer.objects.filter(
                question_id=5,
                text=str(business_type_id)
            ).first()
            if answer:
                return answer.question.directions.all()
        return BusinessDirection.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        questions = self.get_questions()
        business_types = self.get_business_types()
        business_type_id = request.GET.get('business_type_id')
        business_directions = self.get_business_directions(business_type_id)
        return self.render_to_response({'questions': questions,
                                        'business_types': business_types,
                                        'business_directions':
                                        business_directions})

    def post(self, request, *args, **kwargs):
        for question in Question.objects.all():
            answer_text = request.POST.get(f'answer_{question.pk}')
            if answer_text:
                Answer.objects.create(question=question, text=answer_text)
        return redirect('next_survey')


class NextSurveyView(LoginRequiredMixin, TemplateView):
    """Функция для продолжения анкетирования на следующей странице."""

    template_name = 'survey/next_survey.html'

    def get_questions(self):
        return Question.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        questions = self.get_questions()
        return self.render_to_response({'questions': questions})

    def post(self, request, *args, **kwargs):
        for question in Question.objects.all():
            answer_text = request.POST.get(f'answer_{question.pk}')
            if answer_text:
                Answer.objects.create(question=question, text=answer_text)
        return render(request, 'survey/complete_survey.html')


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
