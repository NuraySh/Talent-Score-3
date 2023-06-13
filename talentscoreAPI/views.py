from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from talentscoreAPI.models import *
from talentscoreAPI.serializers import *
from rest_framework import generics


class FormView(APIView):
    def get(self, request):
        stages = Form.objects.all()
        serializer = FormSerializer(stages, many=True, context={"request": request})
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


class QuestionsView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    # filterset_fields = ['question_number', "answers__previous_answer"]

        
    def get(self, request, slug=None, id=None):
        if slug:
            # questions = Questions.objects.filter(slug=slug)
            # if 
            questions = Questions.objects.filter(slug=slug)
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        else:
            questions = Questions.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)

   

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    
    def get(self, request, slug=None, id=None):
        if slug and id:
            try:
                question = Questions.objects.get(slug=slug, answers__id=id)
                serializer = QuestionSerializer(question, context={'id': id})
                return Response(serializer.data)
            except Questions.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
              
            # if question = ''
    # def get_queryset(self):
    #     slug = self.kwargs.get('slug')
    #     a_id = self.kwargs.get('id')
    #     queryset = Questions.objects.filter(slug=slug, answer__id = a_id)
    #     return queryset
        
    


class AnswerDetailView(generics.RetrieveAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(question__slug=slug)
        return queryset
    

class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        previous_answer = self.kwargs.get('previous_answer')
        queryset = Answers.objects.filter(question__slug=slug, previous_answer=previous_answer)
        return queryset
