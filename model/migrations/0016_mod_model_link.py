# Generated by Django 3.2 on 2021-05-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0015_mod_model_author_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='model_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
