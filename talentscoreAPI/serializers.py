from rest_framework import serializers

from talentscoreAPI.models import Answers, Form, Questions, SubStage


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ["id", "question", "answer", "previous_answer"]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    substages =serializers.StringRelatedField(source='substage')

    class Meta:
        model = Questions
        fields = ["substages", "id", "question", "slug", "answer", "question_depends_answer"]


class SubStageSerializer(serializers.ModelSerializer):
    # questions = QuestionSerializer(many=True)
    all_questions = serializers.StringRelatedField(many=True, source='questions')

    class Meta:
        model = SubStage
        fields = ["substage", "all_questions"]


class FormSerializer(serializers.ModelSerializer):
    sub_stages = SubStageSerializer(many=True)


    class Meta:
        model = Form
        fields = ["stage", "sub_stages"]


