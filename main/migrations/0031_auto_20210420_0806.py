# Generated by Django 3.2 on 2021-04-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='model_tags',
            field=models.JSONField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mod',
            name='model_tool',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
