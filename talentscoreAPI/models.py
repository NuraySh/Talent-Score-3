from django.db import models
from django.utils.text import slugify

class Form(models.Model):
    stage = models.CharField(max_length=155)

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"

    def __str__(self):
        return self.stage


class SubStage(models.Model):
    substage = models.CharField(max_length=155)
    stage = models.ForeignKey(Form, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sub Stage"
        verbose_name_plural = "Sub Stages"

    def __str__(self):
        return self.substage


class Questions(models.Model):
    question = models.CharField(max_length=155)
    question_number = models.CharField(max_length=155, default='1')
    previous_question = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    question_type = models.CharField(max_length=50, default="input")
    slug = models.SlugField(null=True, blank=True)  # Add the slug field
    substage = models.ForeignKey(SubStage, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.substage)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question
    

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option_field = models.ManyToManyField(Questions, related_name='option_field')
    answer_text = models.CharField(max_length=255, null=True, blank=True)
    previous_answer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        if  self.answer_text == None:
            return 'input'
        return self.answer_text
    




# substagede question ve ona uygun cavablar
# question-list/{id} == cavab getirir
# admin panel configuration question choices
# question type (input, button, select)

#questions-list/{slug}/{id}



