# Generated by Django 4.2.2 on 2023-06-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talentscoreAPI", "0003_answers_previous_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="questions",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
