# Generated by Django 4.2.1 on 2023-05-17 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0004_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blog_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=80)),
                ("email", models.EmailField(max_length=254)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "ordering": ["created"],
                "indexes": [
                    models.Index(
                        fields=["created"], name="blog_commen_created_0e6ed4_idx"
                    )
                ],
            },
        ),
    ]
