# Generated by Django 4.1.4 on 2022-12-09 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("snippets", "0002_alter_snippet_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="snippet",
            name="highlight",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="snippet",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="snippets",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="snippet",
            name="code",
            field=models.TextField(),
        ),
    ]
