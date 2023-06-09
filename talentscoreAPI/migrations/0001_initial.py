# Generated by Django 4.2.2 on 2023-06-12 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stage", models.CharField(max_length=155)),
            ],
            options={
                "verbose_name": "Stage",
                "verbose_name_plural": "Stages",
            },
        ),
        migrations.CreateModel(
            name="SubStage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("substage", models.CharField(max_length=155)),
                (
                    "stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talentscoreAPI.form",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sub Stage",
                "verbose_name_plural": "Sub Stages",
            },
        ),
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=155)),
                ("question_type", models.CharField(default="input", max_length=50)),
                (
                    "previous_question",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="talentscoreAPI.questions",
                    ),
                ),
                (
                    "substage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talentscoreAPI.substage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
            },
        ),
        migrations.CreateModel(
            name="Answers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "answer_text",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="talentscoreAPI.questions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Answer",
                "verbose_name_plural": "Answers",
            },
        ),
    ]
