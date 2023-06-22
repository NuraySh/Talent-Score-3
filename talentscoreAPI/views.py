from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from talentscoreAPI.models import Answers, Questions, SubStage
from talentscoreAPI.serializers import (AnswerSerializer, QuestionSerializer,
                                        SubStageSerializer)


class SubStageView(APIView):
    def get(self, request):
        substage = SubStage.objects.all()
        serializer = SubStageSerializer(substage, many=True)
        return Response(serializer.data)


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Questions.objects.select_related('substage').prefetch_related('question_depends_answer').prefetch_related(
        Prefetch('answers', queryset=Answers.objects.all())
    ).all()

        slug = self.kwargs.get("slug")
        id = self.kwargs.get("id")

        if slug and id:
            questions = queryset.filter(slug=slug, question_depends_answer__id=id)
            if not questions.exists():
                next_stage_questions = queryset.filter(substage__substage='Olympiad Questions')
                return next_stage_questions
            return questions
        elif slug:
            questions = queryset.filter(slug=slug)
            return questions
        else:
            return queryset

    


class AnswerDetailView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        previous_answer = self.kwargs.get("previous_answer")
        queryset = Answers.objects.filter(
            question__slug=slug, previous_answer=previous_answer
        )
       
        return queryset
