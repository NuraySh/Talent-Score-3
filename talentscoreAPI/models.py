from django.db import models

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
    substage = models.ForeignKey(SubStage, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, null=True)
    
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.answer