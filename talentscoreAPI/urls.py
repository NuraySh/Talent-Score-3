from django.urls import path
from talentscoreAPI.views import *

urlpatterns = [
    
    path("question-list", QuestionsView.as_view(), name="question-list"),
    path("question-list/<slug:slug>/", QuestionsView.as_view(), name="question"),
    path('question-list/<slug:slug>/<int:id>/', AnswerDetailView.as_view(), name='answer-detail'),
    # path('question-list/<slug:slug>/<int:id>/', QuestionDetailView.as_view()), 
  
    path('question-list/<slug:slug>/options/<int:previous_answer>/', AnswerListView.as_view(), name='answer-list'),
]

    # path('question-list/<slug:sl  ug>/<int:previous_answer>/',  AnswerListView.as_view(), name='answer-detal-list')






    # path("form", FormView.as_view(), name="stage"),
    # path("substage", SubStageView.as_view(), name="substage"),
    # path("questions", QuestionsView.as_view(), name="questions"),
    # path("answers", AnswersView.as_view(), name="answers"),
    # path("questions/<int:question_id>/", QuestionsView.as_view(), name="questionlist"),




#questionlist