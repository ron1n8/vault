# Generated by Django 3.2 on 2021-05-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_foll_author_favs'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bought',
            field=models.JSONField(default=[]),
        ),
    ]
