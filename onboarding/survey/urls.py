from django.urls import path

from survey.views import (CustomLoginView, CustomLogoutView,
                          CustomRegisterView, survey_view)

urlpatterns = [
    path('login/', CustomLoginView.as_view(
        template_name='registration/login.html'
        ), name='login'),
    path('register/', CustomRegisterView.as_view(
        template_name='registration/register.html'
        ), name='register'),
    path('logout/', CustomLogoutView.as_view(
        template_name='registration/logout.html'
        ), name='logout'),
    # path('', SurveyView.as_view(
    #     ), name='question'),
    # path('next_survey/', NextSurveyView.as_view(), name='next_survey'),
    path('<int:question_id>/', survey_view, name='survey_question'),
]
