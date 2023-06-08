from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from talentscoreAPI.models import *
from talentscoreAPI.serializers import *



class FormView(APIView):
    
    def get(self, request):
        stages = Form.objects.all()
        serializer = FormSerializer(stages, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubStageView(APIView):
    def get(self, request):
        substages = SubStage.objects.all()
        serializer = SubStageSerializer(substages, many=True)
        return Response(serializer.data)


class QuestionsView(APIView):
    
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswersView(APIView):
    
    def get(self, request):
        answers = Answers.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


