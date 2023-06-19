from django.urls import path

from talentscoreAPI.views import (AnswerDetailView, QuestionListView,
                                  SubStageView)

urlpatterns = [
    path("question-list", SubStageView.as_view(), name="question-list"),
    path("question-list/<slug:slug>/", QuestionListView.as_view()),
    path("question-list/<slug:slug>/<int:id>/", QuestionListView.as_view()),
    path(
        "question-list/<slug:slug>/options/<int:previous_answer>/",
        AnswerDetailView.as_view(),
        name="answer-list",
    ),
]
