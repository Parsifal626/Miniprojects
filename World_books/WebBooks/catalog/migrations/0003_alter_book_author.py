# Generated by Django 4.2 on 2023-04-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_author_book_bookinstance_genre_language_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(
                help_text="Выберите автора книги",
                to="catalog.author",
                verbose_name="Автор книги",
            ),
        ),
    ]
