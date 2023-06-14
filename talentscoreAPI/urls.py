from django.urls import path
from talentscoreAPI.views import *

urlpatterns = [
    
    path('question-list', QuestionListView.as_view(), name='question-list'),
    path('question-list/<slug:slug>/', QuestionListView.as_view(), name='question-list-by-substage'),
    # path('question-list/answer/<slug:slug>/', QuestionDetailView.as_view(), name='question-list-by-answer'),
    path('answer-list', AnswerListView.as_view(), name='answer-list'),
    path('answer-list/<slug:slug>/<int:id>/', AnswerListView.as_view(), name='answer-list'),
    path('question-list/<slug:slug>/options/<int:previous_answer>/', AnswerListView.as_view(), name='answer-list'),
    path('question-list/<slug:slug>/<int:id>/', AnswerDetailView.as_view(), name='answer-detail'),
]


#general question list
#question list by substage

