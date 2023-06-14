# Generated by Django 4.2.2 on 2023-06-14 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("talentscoreAPI", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answers",
            old_name="answer_text",
            new_name="answer",
        ),
        migrations.RemoveField(
            model_name="questions",
            name="previous_question",
        ),
        migrations.AddField(
            model_name="answers",
            name="previous_answer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="talentscoreAPI.answers",
            ),
        ),
        migrations.AddField(
            model_name="answers",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="questions",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]