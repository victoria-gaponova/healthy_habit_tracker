# Generated by Django 4.2.7 on 2023-11-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                blank=True,
                help_text="вознаграждение для пользователя за выполнение привычки",
                max_length=300,
                null=True,
            ),
        ),
    ]
