from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from talentscoreAPI.models import Answers, Questions, SubStage
from talentscoreAPI.serializers import (AnswerSerializer, QuestionSerializer,
                                        SubStageSerializer)


class SubStageView(APIView):
    def get(self, request):
        substages = SubStage.objects.all()
        serializer = SubStageSerializer(substages, many=True)
        return Response(serializer.data)


class QuestionListView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, slug=None, id=None):
        
        if slug and id:
            questions = Questions.objects.filter(slug=slug, question_depends_answer__id=id)
            if not questions.exists():
                next_stage_questions = Questions.objects.filter(substage__substage='Olympiad Questions')
                serializer = QuestionSerializer(next_stage_questions, many=True)
                return Response(serializer.data)
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
           
        elif slug:
            # Filter questions based on the provided slug
            questions = Questions.objects.filter(slug=slug)
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)


class AnswerDetailView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        previous_answer = self.kwargs.get("previous_answer")
        queryset = Answers.objects.filter(
            question__slug=slug, previous_answer=previous_answer
        )
        return queryset
