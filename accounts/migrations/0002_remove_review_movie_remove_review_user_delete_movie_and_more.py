# Generated by Django 5.1.1 on 2024-11-06 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
    ]
