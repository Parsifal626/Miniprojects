# Generated by Django 4.2 on 2023-04-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите Жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.ForeignKey(help_text='Изменить состояние экемпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус экземпляра книги'),
        ),
    ]
