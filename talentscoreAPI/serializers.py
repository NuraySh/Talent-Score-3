from rest_framework import serializers

from talentscoreAPI.models import Answers, Form, Questions, SubStage


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answers
        fields = ["id", "question", "answer", "previous_answer"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Questions
        fields = ["id", "question", "slug", "answers", "question_depends_answer"]


class SubStageSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = SubStage
        fields = ["substage", "questions"]


class FormSerializer(serializers.ModelSerializer):
    sub_stages = SubStageSerializer(many=True)


    class Meta:
        model = Form
        fields = ["stage", "sub_stages"]


