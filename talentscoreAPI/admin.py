from django.contrib import admin
from talentscoreAPI.models import *

admin.site.register(Form)
# admin.site.register(QuestionFlow)

class AnswerOptionInline(admin.TabularInline):
    model = Answers
    extra = 2

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "substage", "question", "question_type"]
    inlines = [AnswerOptionInline]

# class QuestionInline(admin.TabularInline):
#     model = Questions
#     extra = 2

# class SubStageAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]


class AnswersAdmin(admin.ModelAdmin):
    list_display = ["id", 'question', 'previous_answer', 'answer' ]

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SubStage)
admin.site.register(Answers, AnswersAdmin)

