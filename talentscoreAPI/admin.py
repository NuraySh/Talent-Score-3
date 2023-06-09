from django.contrib import admin
from talentscoreAPI.models import *

admin.site.register(Form)
# admin.site.register(SubStage)
admin.site.register(Answers)
# admin.site.register(Questions)

# class AnswerOptionInline(admin.TabularInline):
#     model = Answers
#     extra = 2

# # class VariationInline(admin.TabularInline):
# #     model = Answers
# #     extra = 2

# # class AnswersAdmin(admin.ModelAdmin):
# #     inlines = [VariationInline]


# class OptionInline(admin.TabularInline):
#     model = Answers
#     extra = 2
class AnswerOptionInline(admin.TabularInline):
    model = Answers
    extra = 2


# class AnswersAdmin(admin.ModelAdmin):
#     inlines = [OptionInline]
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "substage", "question", "question_type"]
    inlines = [AnswerOptionInline]

class QuestionInline(admin.TabularInline):
    model = Questions
    extra = 2
class SubStageAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Questions, QuestionsAdmin)
admin.site.register(SubStage, SubStageAdmin)


# class AnswerOptionInline(admin.TabularInline):
#     model = AnswerOption
#     extra = 1

# class Variation2AInline(admin.TabularInline):
#     model = Answers
#     extra = 0
#     verbose_name_plural = "Variation 2A Answers"

#     def get_formset(self, request, obj=None, **kwargs):
#         formset = super().get_formset(request, obj, **kwargs)
#         formset.extra = 2  # Display 2 answer forms for variation 2A
#         return formset

# class Variation2BInline(admin.TabularInline):
#     model = Answers
#     extra = 0
#     verbose_name_plural = "Variation 2B Answers"

#     def get_formset(self, request, obj=None, **kwargs):
#         formset = super().get_formset(request, obj, **kwargs)
#         formset.extra = 3  # Display 3 answer forms for variation 2B
#         return formset

# class QuestionsAdmin(admin.ModelAdmin):
#     inlines = [AnswerOptionInline]

#     def get_inline_instances(self, request, obj=None):
#         if obj:
#             if obj.variation == '2A':
#                 return [Variation2AInline(self.model, self.admin_site)]
#             elif obj.variation == '2B':
#                 return [Variation2BInline(self.model, self.admin_site)]
#         return []

# admin.site.register(Questions, QuestionsAdmin)
