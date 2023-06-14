from rest_framework import serializers
from talentscoreAPI.models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ["id",  "question", "answer", "previous_answer", "slug"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Questions
        fields = ["id", "question", "slug",  "answers"]

    def get_answers(self, question):
        answers = question.answers_set.all()
        answer_serializer = AnswerSerializer(answers, many=True, context=self.context)
        return answer_serializer.data


class SubStageSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = SubStage
        fields = ["substage", "questions"]

    def get_questions(self, sub_stage):
        questions = sub_stage.questions_set.all()
        question_serializer = QuestionSerializer(
            questions, many=True, context=self.context
        )
        return question_serializer.data


class FormSerializer(serializers.ModelSerializer):
    sub_stages = serializers.SerializerMethodField()

    class Meta:
        model = Form
        fields = ["stage", "sub_stages"]

    def get_sub_stages(self, stage):
        sub_stages = stage.substage_set.all()
        sub_stage_serializer = SubStageSerializer(
            sub_stages, many=True, context=self.context
        )
        return sub_stage_serializer.data
