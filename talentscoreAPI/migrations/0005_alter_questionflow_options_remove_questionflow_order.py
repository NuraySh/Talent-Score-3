# Generated by Django 4.2.2 on 2023-06-14 08:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("talentscoreAPI", "0004_alter_questionflow_question"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="questionflow",
            options={
                "verbose_name": "Question Flow",
                "verbose_name_plural": "Question Flows",
            },
        ),
        migrations.RemoveField(
            model_name="questionflow",
            name="order",
        ),
    ]