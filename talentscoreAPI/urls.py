from django.urls import path
from talentscoreAPI.views import *

urlpatterns = [
    path("form", FormView.as_view(), name="stage"),
    path("substage", SubStageView.as_view(), name="substage"),
    path("questions", QuestionsView.as_view(), name="questions"),
    path("answers", AnswersView.as_view(), name="answers"),
]