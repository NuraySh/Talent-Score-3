from django.contrib import admin
from talentscoreAPI.models import *

admin.site.register(Form)

class AnswerOptionInline(admin.TabularInline):
    model = Answers
    extra = 2

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "substage", "question", "question_number", "question_type"]
    inlines = [AnswerOptionInline]

# class QuestionInline(admin.TabularInline):
#     model = Questions
#     extra = 2

# class SubStageAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]


class AnswersAdmin(admin.ModelAdmin):
    list_display = ["id", 'question', 'previous_answer', 'answer_text' ]

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SubStage)
admin.site.register(Answers, AnswersAdmin)

