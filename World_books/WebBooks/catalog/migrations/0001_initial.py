# Generated by Django 4.2 on 2023-04-27 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyModelName",
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
                    "my_field_name",
                    models.CharField(help_text="Не более 20 символов", max_length=20),
                ),
            ],
        ),
    ]
