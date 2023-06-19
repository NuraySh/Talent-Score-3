from django.contrib import admin

from talentscoreAPI.models import Answers, Form, Questions, SubStage

admin.site.register(Form)
admin.site.register(SubStage)

class AnswerOptionInline(admin.TabularInline):
    model = Answers
    extra = 2

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "substage", "question", "question_type"]
    inlines = [AnswerOptionInline]

class AnswersAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "previous_answer", "answer"]


admin.site.register(Questions, QuestionsAdmin)

admin.site.register(Answers, AnswersAdmin)
