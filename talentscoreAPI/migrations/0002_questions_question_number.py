# Generated by Django 4.2.2 on 2023-06-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talentscoreAPI", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="questions",
            name="question_number",
            field=models.CharField(default="1", max_length=155),
        ),
    ]
